from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.controllers.chat_controller import run_chat_with_tool
from app.utils.image_generator import generate_book_image
from app.models.request_models import ChatRequest, ImageRequest, ListenRequest
from app.utils.history_logger import log_event
import uuid

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    try:
        request_id = str(uuid.uuid4())
        response = run_chat_with_tool(request.query, return_as_string=True)

        if "message" not in response:
            response = {
                "title": "",
                "message": "No response.",
                "short_summary": "",
                "full_summary": "",
                "themes": []
            }

        response["request_id"] = request_id
        log_event({
            "type": "chat",
            "request_id": request_id,
            "user_query": request.query,
            **response
        })

        return response

    except Exception as e:
        print("Error in /chat:", e)
        return JSONResponse(
            content={"message": " Internal server error."}, status_code=500
        )


@app.post("/generate-image")
async def generate_image(request: ImageRequest):
    # body = await request.json()
    title = request.title
    if not title:
        return JSONResponse(content={"error": "No title provided."}, status_code=400)

    try:
        image_url = generate_book_image(request.title)

        event = {
            "type": "image",
            "request_id": request.request_id or str(uuid.uuid4()),
            "title": request.title,
            "image_url": image_url
        }
        log_event(event)

        return JSONResponse(content={"image_url": image_url})
    except Exception as e:
        print(" Image generation error:", e)
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.post("/listen")
async def listen_event(request: ListenRequest):
    try:
        log_event({
            "type": "listen",
            "request_id": request.request_id,
            "text": request.text
        })
        return {"status": "ok"}
    except Exception as e:
        print("Error in /listen:", e)
        return JSONResponse(content={"error": str(e)}, status_code=500)
