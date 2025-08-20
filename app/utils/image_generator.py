from openai import OpenAI
import os
import webbrowser

def generate_book_image(title: str) -> str:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    prompt = f"A representative book cover illustration or scene inspired by the book '{title}'"

    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        n=1
    )

    image_url = response.data[0].url
    print(f"\n Generated image: {image_url}")
    webbrowser.open(image_url)
    return image_url 
