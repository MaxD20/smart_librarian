from services.embedding_service import load_book_summaries, embed_summaries_to_chroma
import os

summaries = load_book_summaries("data/book_summaries.txt")
embed_summaries_to_chroma(summaries, openai_api_key=os.getenv("OPENAI_API_KEY"))