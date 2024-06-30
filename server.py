import asyncio
import json

from typing import Any

from fastapi import Body, FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse

import uvicorn

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8081",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


hostName = "http://localhost:8000"
urlPath = "/agents"

@app.get("/agents/list")
def agentList():
    dataSet = [{
        "name": "echoAgent",
        "category": "test",
    }, {
        "name": "copyAgent",
        "category": "test",
    }]
    
    def conv(data):
        return {
            "agentId": data.get("name"),
            "name": data.get("name"),
            "url": hostName + urlPath + "/" + data.get("name"),
            "category": data.get("category"),
            "inputs": [],
            "output": [],
            "stream": False,
        }
    ret = list(map(conv, dataSet))
    print(ret)
    
    agentsList = { "agents": ret }
    return JSONResponse(content=agentsList)


@app.post("/agents/echoAgent")
def echo(payload: Any = Body(None)):
    inputs = payload.get("inputs")
    
    return JSONResponse(content=inputs)

@app.post("/agents/copyAgent")
def copy(payload: Any = Body(None)):
    inputs = payload.get("inputs") 
    
    return JSONResponse(content=inputs[0])

@app.post("/agents/streamAgent")
async def stream_json_example():
    async def generate_json_data():
        for i in range(10):
            await asyncio.sleep(1.0)
            yield f"{i}\n"

        yield "___END___";
        yield "0123456789";

    return StreamingResponse(content=generate_json_data(), media_type="text/event-stream")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
