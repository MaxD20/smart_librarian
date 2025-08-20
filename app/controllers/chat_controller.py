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

    if user_query.lower().startswith("what is the summary of") or "full summary of" in user_query.lower():
    # Try to extract title from query
        cleaned_query = user_query.strip().rstrip(" ?.!").strip()
        match = re.search(r"(?:summary of|full summary of)\s+['\"]?(.+?)['\"]?$", cleaned_query, re.IGNORECASE)
        if match:
            title = match.group(1).strip()
            summary = get_summary_by_title(title)
            return {
                "title": title,
                "message": summary
            }

    title, short_summary = semantic_search(user_query, openai_api_key=os.getenv("OPENAI_API_KEY"))

    system_prompt = "You are a helpful AI librarian that recommends books based on user interests."

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"I'm interested in: {user_query}"},
        {"role": "user", "content": f"A recommended book is '{title}' because: {short_summary}. Please recommend it conversationally"},
    ]

    response = client.chat.completions.create(
        model="gpt-4.1-nano",
        messages=messages,
        tools=[get_summary_tool],
        #tool_choice="auto"
    )

    content = response.choices[0].message.content
    
    print(f"\n Recommended book is: {title}")
    print(f"\n LLM Suggestion:\n {content}")

    
    if return_as_string:
        return {
            "title": title,
            "message": content,
            "summary": short_summary
        }

    # CLI mode interactivity
    speech_output = content

    hear = input("\nWould you like to hear this? (y/n): ")
    if hear.lower() == "y":
        speak(speech_output)

    follow_up = input("\nWould you like the full summary of this book? (y/n): ")
    full_summary = None
    if follow_up.lower() == "y":
        tool_messages = messages + [
            {"role": "user", "content": f"Can you give me the full summary of '{title}'?"}
        ]
        response = client.chat.completions.create(
            model="gpt-4.1-nano",
            messages=tool_messages,
            tools=[get_summary_tool],
            #tool_choice="auto"
        )

        tool_call = response.choices[0].message.tool_calls[0]
        arguments = json.loads(tool_call.function.arguments)
        book_title = arguments.get("title", title)
        full_summary = get_summary_by_title(book_title)

        print(f"\n Full summary for '{book_title}':\n{full_summary}")

        hear_full = input("\nHear full summary? (y/n): ")
        if hear_full.lower() == "y":
            speak(full_summary)

    generate = input("\nWould you like to see a generated cover or scene from the book? (y/n): ")
    if generate.lower() == "y":
        book_title_to_use = book_title if full_summary else title
        prompt = f"Generate a representative book cover or scene for '{book_title_to_use}'"
        generate_book_image(prompt)

    if return_as_string:
        return {
            "title": title,
            "message": full_summary if follow_up.lower() == "y" and full_summary else content
        }
# #######
# from openai import OpenAI
# import os
# import json

# from app.services.embedding_service import semantic_search
# from app.services.tool_functions import get_summary_by_title
# from app.utils.text_to_speech import speak
# from app.utils.image_generator import generate_book_image

# get_summary_tool = {
#     "type": "function",
#     "function": {
#         "name": "get_summary_by_title",
#         "description": "Return the full summary for a given book title.",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "title": {
#                     "type": "string",
#                     "description": "Exact title of the book"
#                 }
#             },
#             "required": ["title"]
#         }
#     }
# }

# def get_summary_by_title(title: str) -> str:
#     file_path = "data/book_summaries.txt"
#     try:
#         with open(file_path, "r", encoding="utf-8") as f:
#             for line in f:
#                 if line.startswith("## Title:") and "::" in line:
#                     parts = line[len("## Title:"):].strip().split("::", 1)
#                     if len(parts) == 2:
#                         book_title, summary = parts
#                         if book_title.strip().lower() == title.strip().lower():
#                             return summary.strip()
#         return f"⚠️ No full summary found for the title: {title}"
#     except Exception as e:
#         return f"❌ Error reading summaries file: {str(e)}"

# def run_chat_with_tool(user_query: str, return_as_string: bool = False):
#     offensive_keywords = ["idiot", "stupid", "hate", "kill", "racist", "profanity"]
#     if any(bad_word in user_query.lower() for bad_word in offensive_keywords):
#         warning = " Smart librarian: I'm here to help with book suggestions, but let's keep our conversation respectful. "
#         print(f"\n {warning}")
#         return warning if return_as_string else None

#     client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
#     title, short_summary = semantic_search(user_query, openai_api_key=os.getenv("OPENAI_API_KEY"))

#     system_prompt = "You are a helpful AI librarian that recommends books based on user interests."

#     messages = [
#         {"role": "system", "content": system_prompt},
#         {"role": "user", "content": f"I'm interested in: {user_query}"},
#         {"role": "user", "content": f"A recommended book is '{title}' because: {short_summary}. Please recommend it conversationally"},
#     ]

#     response = client.chat.completions.create(
#         model="gpt-4.1-nano",
#         messages=messages,
#         tools=[get_summary_tool],
#         tool_choice="auto"
#     )

#     content = response.choices[0].message.content
#     print(f"\n Recommended book is: {title}")
#     print(f"\n LLM Suggestion:\n {content}")

#     if return_as_string:
#         return {
#             "title": title,
#             "message": content
#         }

#     speech_output = content
#     hear = input("\nWould you like to hear this? (y/n): ")
#     if hear.lower() == "y":
#         speak(speech_output)

#     follow_up = input("\nWould you like the full summary of this book? (y/n): ")
#     full_summary = None
#     if follow_up.lower() == "y":
#         tool_messages = messages + [
#             {"role": "user", "content": f"Can you give me the full summary of '{title}'?"}
#         ]
#         response = client.chat.completions.create(
#             model="gpt-4.1-nano",
#             messages=tool_messages,
#             tools=[get_summary_tool],
#             tool_choice="auto"
#         )

#         tool_call = response.choices[0].message.tool_calls[0]
#         arguments = json.loads(tool_call.function.arguments)
#         book_title = arguments.get("title")
#         full_summary = get_summary_by_title(book_title)

#         print(f"\n Full summary for '{book_title}':\n{full_summary}")
#         hear_full = input("\nHear full summary? (y/n): ")
#         if hear_full.lower() == "y":
#             speak(full_summary)

#     generate = input("\nWould you like to see a generated cover or scene from the book? (y/n): ")
#     if generate.lower() == "y":
#         book_title_to_use = book_title if full_summary else title
#         prompt = f"Generate a fantasy book cover or scene for '{book_title_to_use}'"
#         generate_book_image(prompt)

#     if return_as_string:
#         return {
#             "title": title,
#             "message": full_summary if follow_up.lower() == "y" and full_summary else content
#         }
