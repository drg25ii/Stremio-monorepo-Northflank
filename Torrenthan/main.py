import os
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="Torrenthan")

@app.get("/")
async def root():
    return {"status": "ok", "service": "torrenthan", "port": int(os.getenv("PORT", "7860"))}

@app.get("/health")
async def health():
    return JSONResponse({"ok": True})
