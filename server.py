import os
import uvicorn
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI()
ui_elements = []

def set_elements(elements):
    global ui_elements
    ui_elements = elements

@app.get("/")
async def get_ui():
    if os.path.exists("index.html"):
        with open("index.html", "r") as f:
            return HTMLResponse(content=f.read())
    return HTMLResponse(content="<h1>Index.html not found</h1>")

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_json(ui_elements)
    while True:
        try:
            await websocket.receive_text()
        except:
            break

def run_server():
    uvicorn.run(app, host="127.0.0.1", port=8501)