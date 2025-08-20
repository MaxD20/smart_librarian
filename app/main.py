from app.controllers.chat_controller import run_chat_with_tool
import os

def main():
    print("\n Hi user ! You are at Smart Librarian, feel free to ask for a book recommendation or a theme!")
    print("(Type 'q' to quit)\n")

    while True:
        user_query = input("\nWhat kind of book are you looking for?\n")
        if user_query.lower().strip() == "q":
            print("Bye!")
            break

        if len(user_query.strip()) == 0:
            print("Enter a valid query.")
            continue

        run_chat_with_tool(user_query)

if __name__ == "__main__":
    main()


