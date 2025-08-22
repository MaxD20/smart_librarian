import chromadb
from tqdm import tqdm
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

CHROMA_PATH = "./chromadb_store"
COLLECTION_NAME = "book_summaries"


def parse_summary_line(line: str):
    clean_line = line.replace("## Title: ", "").strip()
    if "::" not in clean_line:
        raise ValueError("Line missing '::' separator")
    title, rest = clean_line.split("::", 1)
    title = title.strip()
    if "||themes:" in rest:
        short_summary, themes_str = rest.split("||themes:", 1)
        short_summary = short_summary.strip()
        themes = [t.strip() for t in themes_str.split(";") if t.strip()]
    else:
        short_summary = rest.strip()
        themes = []
    return title, short_summary, themes


def load_book_summaries(file_path: str):
    items = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("## Title:"):
                try:
                    title, short_summary, themes = parse_summary_line(line)
                    items.append((title, short_summary, themes))
                except Exception as e:
                    print("Skipping malformed line:", line.strip(), "| Error:", e)
    return items


def embed_summaries_to_chroma(summaries, openai_api_key: str, reset: bool = False):
    client = chromadb.PersistentClient(path=CHROMA_PATH)

    if reset:
        try:
            client.delete_collection(COLLECTION_NAME)
        except Exception:
            pass

    embedding_function = OpenAIEmbeddingFunction(
        api_key=openai_api_key, model_name="text-embedding-3-small"
    )

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME, embedding_function=embedding_function
    )

    ids, documents, metadatas = [], [], []

    for idx, (title, short_summary, themes) in enumerate(
        tqdm(summaries, desc="Embedding summaries")
    ):
        themes_str = ", ".join(themes) if themes else ""
        if themes_str:
            document_text = f"{short_summary}\nThemes: {themes_str}"
        else:
            document_text = short_summary

        ids.append(f"book_{idx}")
        documents.append(document_text)
        metadatas.append({"title": title, "themes": themes_str})

    if ids:
        collection.add(documents=documents, metadatas=metadatas, ids=ids)
        print(f"Embedded {len(ids)} items into '{COLLECTION_NAME}' at {CHROMA_PATH}")
    else:
        print("No items to embed.")


def semantic_search(query: str, openai_api_key: str, top_k: int = 1):
    client = chromadb.PersistentClient(path=CHROMA_PATH)

    embedding_function = OpenAIEmbeddingFunction(
        api_key=openai_api_key, model_name="text-embedding-3-small"
    )

    collection = client.get_collection(
        name=COLLECTION_NAME, embedding_function=embedding_function
    )

    results = collection.query(query_texts=[query], n_results=top_k)

    if not results or not results.get("documents") or not results["documents"][0]:
        return "", "", []

    metadata = results["metadatas"][0][0] if results.get("metadatas") else {}
    document = results["documents"][0][0]
    title = metadata.get("title", "")
    themes_str = metadata.get("themes", "") or ""
    themes = [t.strip() for t in themes_str.split(",") if t.strip()]

    return title, document, themes
