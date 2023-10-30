from fastapi import FastAPI, WebSocket
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

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

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Echo: {data}")

@app.get("/api/chat/")
async def read_chat(message: dict):
    # Generate a response
    answer = f"Your {i} mock answer..."  # Replace with your logic
    i += 1
    # Package and return the response
    return {'text': answer, 'isUser': False, 'time': int(datetime.now().timestamp())}

i = 0
