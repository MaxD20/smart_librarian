import os
import chromadb
from tqdm import tqdm
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

def load_book_summaries(file_path: str):
    summaries = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("## Title:"):
                clean_line = line.replace("## Title: ", "").strip()
                if "::" in clean_line:
                    title, summary = clean_line.split("::", 1)
                    summaries.append((title.strip(), summary.strip()))
                else:
                    print(f"Malformed line: {line.strip()}")
    return summaries                       

def embed_summaries_to_chroma(summaries, openai_api_key: str):
    # Embed the summaries with OpenAI's text embedding 3 small and store in a local ChromaDB collection for semnatic search
    client = chromadb.PersistentClient(path="./chromadb_store")

    embedding_function = OpenAIEmbeddingFunction(
        api_key=openai_api_key,
        model_name="text-embedding-3-small"
    )

    collection = client.get_or_create_collection(
        name="book_summaries",
        embedding_function=embedding_function
    )

    ids, documents, metadatas = [], [], []
    for idx, (title, summary) in enumerate(tqdm(summaries, desc="Embedding summaries")):
        ids.append(f"book_{idx}")
        documents.append(summary)
        metadatas.append({"title": title})

    collection.add(documents=documents, metadatas=metadatas, ids=ids)
    print("Book summaries embedded well and stored in ChromaDB.")


def semantic_search(query: str, openai_api_key: str, top_k: int = 1):
    # Perform semantic search in ChromaDB for a user query
    client = chromadb.PersistentClient(path="./chromadb_store")

    embedding_function = OpenAIEmbeddingFunction(
        api_key = openai_api_key,
        model_name = "text-embedding-3-small"
    )

    collection = client.get_collection(
        name="book_summaries",
        embedding_function=embedding_function
    )            

    results = collection.query(
        query_texts=[query],
        n_results=top_k
    )

    title = results['metadatas'][0][0]['title']
    summary = results['documents'][0][0]
    return title, summary 