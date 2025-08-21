# ##Var buna###
from openai import OpenAI
import os
import json
import re
from app.services.embedding_service import semantic_search
from app.services.tool_functions import get_summary_by_title
from app.utils.text_to_speech import speak
from app.utils.image_generator import generate_book_image

get_summary_tool = {
    "type": "function",
    "function": {
        "name": "get_summary_by_title",
        "description": "Return the full summary for a given book title.",
        "parameters": {
            "type": "object",
            "properties": {
                "title": {
                    "type": "string",
                    "description": "Exact title of the book"
                }
            },
            "required": ["title"]
        }
    }
}

def run_chat_with_tool(user_query: str, return_as_string: bool = False):
    offensive_keywords = ["idiot", "stupid", "hate", "kill", "racist", "profanity"]
    if any(bad_word in user_query.lower() for bad_word in offensive_keywords):
        warning = " Smart librarian: I'm here to help with book suggestions, but let's keep our conversation respectful. "
        print(f"\n {warning}")
        return warning if return_as_string else None

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # if user_query.lower().startswith("what is the summary of") or "full summary of" in user_query.lower():
    # # Try to extract title from query
    #     cleaned_query = user_query.strip().rstrip(" ?.!").strip()
    #     match = re.search(r"(?:summary of|full summary of)\s+['\"]?(.+?)['\"]?$", cleaned_query, re.IGNORECASE)
    #     if match:
    #         title = match.group(1).strip()
    #         summary = get_summary_by_title(title)
    #         return {
    #             "title": title,
    #             "message": summary,
    #             "summary": summary
    #         }

    title, document, themes = semantic_search(user_query, openai_api_key=os.getenv("OPENAI_API_KEY"))

    # system_prompt = "You are a helpful AI librarian that recommends books based on user interests."

    title = (title or "").strip()
    #short_summary = " ".join((short_summary or "").split())

    if document and "\nThemes:" in document:
        short_summary = document.split("\nThemes:", 1)[0].strip()
    else:
        short_summary = (document or "").strip()

    short_summary = " ".join(short_summary.split())

    try:
        messages = [
            {"role": "system", "content": "You are a librarian assistant. Think silently; do not produce user-facing text."},
            {"role": "user", "content": f"User query: {user_query}"},
            {"role": "assistant", "content": f"RAG result -> title: '{title}', summary: {short_summary}"},
            {"role": "user", "content": "Acknowledge internally only."}
        ]
        _ = client.chat.completions.create(
            model="gpt-4.1-nano",
            messages=messages
        )
    except Exception:
        # If GPT hiccups, still serve RAG output.
        pass

    full_summary = get_summary_by_title(title) or ""

    # Keep the EXACT two-line format for the frontend
    formatted = (
        f"Recommended book: {title}\n"
        f"Short summary of LLM: {short_summary}"
    )
    if full_summary:
        formatted += f"\n\nFull summary:\n{full_summary}"

    print(formatted)


    if return_as_string:
        return {
            "title": title,
            "message": formatted,
            "summary": short_summary,
            "full_summary": full_summary
        }

    # CLI mode interactivity
    speech_output = formatted

    hear = input("\nWould you like to hear this? (y/n): ")
    if hear.lower() == "y":
        speak(speech_output)

    follow_up = input("\nWould you like the full summary of this book? (y/n): ")
    full_summary = None
    if follow_up.lower() == "y":
        full_summary = get_summary_by_title(title) or "No full summary found."
        print(f"\n Full summary for '{title}':\n{full_summary}")
        hear_full = input("\nHear full summary? (y/n): ")
        if hear_full.lower() == "y":
            speak(full_summary)


    generate = input("\nWould you like to see a generated cover or scene from the book? (y/n): ")
    if generate.lower() == "y":
        book_title_to_use = title if full_summary else title
        prompt = f"Generate a representative book cover or scene for '{book_title_to_use}'"
        generate_book_image(prompt)


    if return_as_string:
        return {
            "title": title,
            "message": full_summary if follow_up.lower() == "y" and full_summary else formatted,
            "summary": short_summary
        }