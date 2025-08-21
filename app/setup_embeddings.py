import os
from services.embedding_service import load_book_summaries, embed_summaries_to_chroma

def main():
    
    summaries = load_book_summaries("data/book_summaries.txt")


    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set. Please set it before running.")

  
    embed_summaries_to_chroma(summaries, openai_api_key=api_key)

if __name__ == "__main__":
    main()