
import json
import os


SUMMARY_PATH = os.path.join("data", "book_summaries_dict.json")

try:
    with open(SUMMARY_PATH, "r", encoding="utf-8") as f:
        book_summaries_dict = json.load(f)
except FileNotFoundError:
    book_summaries_dict = {}
    print(" book_summaries_dict.json not found. ")

# def get_summary_by_title(title: str) -> str:
#     summary = book_summaries_dict.get(title.strip())
#     if summary:
#         return summary
#     else:
#         return f"Sorry, no full summary found for '{title}'. Please try another title."
    
def get_summary_by_title(title: str) -> str:
    title_clean = title.strip().lower()
    
    for stored_title, summary in book_summaries_dict.items():
        if stored_title.strip().lower() == title_clean:
            return summary
    
    return f"Sorry, no full summary found for '{title}'. Please try another title."