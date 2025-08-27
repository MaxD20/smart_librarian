
import json
import os


SUMMARY_PATH = os.path.join("data", "book_summaries_dict.json")

try:
    with open(SUMMARY_PATH, "r", encoding="utf-8") as f:
        book_summaries_dict = json.load(f)
except FileNotFoundError:
    book_summaries_dict = {}
    print(" book_summaries_dict.json not found. ")

def _extract_full(value):
    if isinstance(value, dict):
        full = value.get("full")
        if isinstance(full, str) and full.strip():
            return full
        short = value.get("short")
        if isinstance(short, str) and short.strip():
            return short
        return None
    if isinstance(value, str):
        return value
    return None

def get_summary_by_title(title: str) -> str:
    v = book_summaries_dict.get(title)
    full = _extract_full(v) if v is not None else None
    if full:
        return full

    title_clean = title.strip().lower()
    for stored_title, value in book_summaries_dict.items():
        if isinstance(stored_title, str) and stored_title.strip().lower() == title_clean:
            full = _extract_full(value)
            if full:
                return full

    return f"Sorry, no full summary found for '{title}'. Please try another title."