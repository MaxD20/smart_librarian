from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.controllers.chat_controller import run_chat_with_tool
from app.utils.image_generator import generate_book_image
from app.models.request_models import ChatRequest, ImageRequest
# from pydantic import BaseModel

# class ImageRequest(BaseModel):
#     title: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.post("/chat")
# async def chat_endpoint(request: Request):
#     body = await request.json()
#     query = body.get("query")
    
#     if not query:
#         return JSONResponse(content={"message": " No query received."}, status_code=400)

#     try:
#         result = run_chat_with_tool(query, return_as_string=True)
#         if isinstance(result, dict):
#             return JSONResponse(content={"message": result["message"], "title": result["title"]})
#         return JSONResponse(content={"message": result})
#     except Exception as e:
#         print(" Error:", e)
#         return JSONResponse(content={"message": " Internal server error."}, status_code=500)

# @app.post("/generate-image")
# async def generate_image(request: Request):
#     body = await request.json()
#     title = body.get("title")
#     if not title:
#         return JSONResponse(content={"error": "No title provided."}, status_code=400)
    
#     try:
#         image_url = generate_book_image(title)
#         return JSONResponse(content={"image_url": image_url})
#     except Exception as e:
#         print(" Image generation error:", e)
#         return JSONResponse(content={"error": str(e)}, status_code=500)

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    try:
        response = run_chat_with_tool(request.query, return_as_string=True)
        # return {"message": response["message"], "summary": response.get("summary", "")}
        if not response or "message" not in response:
            return {"title": "", "message": "No response.", "summary": ""}
        
        return {
            "title": response.get("title", ""),
            "message": response.get("message", ""),
            "summary": response.get("summary", "")
        }
    except Exception as e:
        print("Error in /chat:", e)
        return JSONResponse(content={"message": " Internal server error."}, status_code=500)

@app.post("/generate-image")
async def generate_image(request: ImageRequest):
    # body = await request.json()
    title = request.title
    if not title:
        return JSONResponse(content={"error": "No title provided."}, status_code=400)
    
    try:
        image_url = generate_book_image(request.title)
        return JSONResponse(content={"image_url": image_url})
    except Exception as e:
        print(" Image generation error:", e)
        return JSONResponse(content={"error": str(e)}, status_code=500)