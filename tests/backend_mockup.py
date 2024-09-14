from fastapi import FastAPI, WebSocket, Response, Header, Body
from fastapi.responses import JSONResponse
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict

# Define the app
app = FastAPI()

# CORS settings
origins = [
  "http://localhost:4200",
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

# Mock chat history
chat_history = {
  "conversation0": [
    {'text': 'Hello', 'isUser': False, 'time': int(datetime.now().timestamp())},
    {'text': 'World', 'isUser': True, 'time': (int(datetime.now().timestamp()) + 1)},
  ],
  "conversation1": [
    {'text': 'Hi', 'isUser': True, 'time': int(datetime.now().timestamp())},
  ],
}

content = {'messageIds': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']}

"""
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Echo: {data}")
"""


@app.get('/api/get/polling')
async def polling():
    return Response(status_code=204)


@app.post("/api/post/message")
async def post_message(message: dict = Body(None)):
    print(message)
    return Response(status_code=201)


@app.get("/api/get/history")
async def get_chat_history(conversationId: str = Header(None)):
    if conversationId is None:
        return JSONResponse(content={"error": "Missing conversationId header"}, status_code=400)
    history_content = chat_history.get(conversationId, [])
    return JSONResponse(content={conversationId: history_content}, status_code=200)
