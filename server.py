from typing import Any

from fastapi import Body, FastAPI
from fastapi.responses import JSONResponse

import uvicorn

app = FastAPI()

@app.post("/agents/echoAgent")
def echo(payload: Any = Body(None)):
    inputs = payload.get("inputs")
    
    return JSONResponse(content=inputs)

@app.post("/agents/copyAgent")
def echo(payload: Any = Body(None)):
    inputs = payload.get("inputs")
    
    return inputs[0]


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
