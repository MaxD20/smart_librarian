# Smart Librarian, AI RAG chatbot with tool

- Maxim Dragos, Data&AI

Smart Librarian is an AI-powered chatbot that recommends books based on user interests.  
It combines **OpenAI GPT** with **RAG (Retrieval-Augmented Generation)** using **ChromaDB** for semantic search,  
and provides **short + full summaries** through a tool function. 

The assistant also supports:
- **Text-to-speech (Listen)**
- **Image generation (Book covers/scenes)**  
- **Interaction logging (chat + images + listen events)** 

## Workflow of RAG chatbot
- recommends books using semantic search over a local vector store (ChromaDB),
- returns a short summary from RAG,
- fetches the full summary via a registered tool (`get_summary_by_title`),
- provides a simple web UI (Vue + vanilla JS),
- logs chat, image-generation, and “listen” events to a local JSON file.

##  Dependencies

- **openai** -> to connect with OpenAI GPT models for embeddings, chat completions, and image generation.  
- **chromadb** -> a lightweight vector database used to store and query book summaries for semantic search (RAG).  
- **pydantic** -> data validation and request/response models in FastAPI.  
- **tqdm** -> provides progress bars for embedding operations.  
- **fastapi** -> the backend framework used to expose endpoints for chat, image generation, and event logging.  
- **uvicorn** -> ASGI server to run the FastAPI app.  
- **sqlalchemy** -> reserved for structured database support
- **requests** -> for making HTTP requests (used internally and can support external API calls).  
- **pyttsx3** -> local text-to-speech engine (the frontend primarily uses the browser’s `SpeechSynthesis`).  
- **flake8** -> linting tool to maintain code quality.  
- **black** -> code formatter to ensure consistent style. 

## Prerequisites

- **Python** 3.10+
- An **OpenAI API key** available as environment variable: `OPENAI_API_KEY`


## Build steps
1. **Clone the repository**
```bash
git clone https://github.com/MaxD20/smart_librarian.git
cd smart_librarian
```

2. **Create and activate a virtual environment**
```
python -m venv .venv
.venv\Scripts\Activate.ps1
```
3. **Install dependencies**
```
pip install -r requirements.txt
```
## Data generation - if needed
- If data/book_summaries.txt and data/book_summaries_dict.json don't exist, they can be generated with
```
python tool/generate_book_summaries.py
```
- If the files already exist in the data/, this step can be skipped

## Initialize the vector store (embeddings)
- Create/update the ChromaDB collection from data/book_summaries.txt:
```
python -m app.setup_embeddings
```
- It parses book_summaries.txt (Short summaries and optional themes)
- Embeds with OpenAI text-embedding-3-small
- Stores them in local ChromaDB folder (./chromadb_store)

## Run the Backend (FastAPI)
- Start the API server:
```
uvicorn fastapi_app:app --reload
```
- Server runs at: http://localhost:8000/docs
- CORS is enabled for the frontend (http://localhost:5173)

- Key endpoints
- POST/chat takes { "query": "..."}, returns recommended title, short summary, and full summary (when available). Also returns a request_id used to correlate UI actions.
- POST / generate-image takes { "title": "...", "request_id": "..."}, returns { "image_url": "..."}. The event is logged.
- POST listen takes { "request_id": "...", "text": "..."} to log "Listen" button presses

- Logging:
All interactions are appended to JSON log (file path defined in app/utils/history_logger.py), under data/.

## Run the Frontend (Vue via static server)
From the project root:
```
cd public
python -m http.server 5173
```

Then open
```
http://localhost:5173
```

- Frontend workflow
- The user types a query and presses Ask.
- The page calls POST /chat and displays "Recommended book" + "Short summary"
- If a full summary is found via the tool, it is appended below the short one.
- If the user enter a bad word in chat, it will be prompted with a warning and the summary of the book won't generate
- The Listen button uses the browser's SpeechSynthesis to read the text and calls POST /listen to log the action.
- The Generate imge button posts to /generate-image, appends the image to chat, and logs the event (title, URL, request id).

Execution flow
- User query, frontend sends {query} to FastAPI /chat
- RAG -> backend runs semantic_search (ChromaDB) to find the best title and short summary and themes
- Tool calling -> backend calls get_summary_by_title(title) to retrieve the full summary from data/book_summaries_dict.json
- Response -> backend returns a combined message (recommendation title + short summary + full summary) and a request_id
- UI Actions
- -> Listen: the frontend uses peechSynthesis and calls /listen with { request_id, text} to log the event
- -> Generate image: the frontend calls /generate-image with {title, request_id}. The backend returns image_url and logs the event. The image is displayed in the chat.

Quality:
- run lint and format:
```
flake8
black .
```

## Proof of concept
RAG chatbot overview<br>
<img src="https://github.com/MaxD20/smart_librarian/blob/96200ce0c65796b76e9d7e48f97f7bb5b0cc5b18/rag_chatbot_overview.png?raw=true" alt="RAG chatbot overview"  width="60%"/>
</br>

## Chat history
- The chat history is presented in data/logs/chat_history.json

Chat history<br>
<img src="https://github.com/MaxD20/smart_librarian/blob/7afe70ed8b154293821194be8bd0dd03a5170381/chat_history.png?raw=true" alt="Chat history" width="60%"/>
</br>
