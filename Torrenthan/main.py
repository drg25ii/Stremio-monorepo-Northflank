import base64
import json
import os
from typing import Any, Dict

from fastapi import FastAPI, HTTPException

app = FastAPI(title="Torrenthan (rebuild)")

def _b64url_decode(s: str) -> Dict[str, Any]:
    # HF/Stremio folosesc frecvent base64url fără padding
    pad = "=" * (-len(s) % 4)
    raw = base64.urlsafe_b64decode((s + pad).encode("utf-8"))
    return json.loads(raw.decode("utf-8"))

@app.get("/")
async def root():
    return {"ok": True, "service": "torrenthan", "hint": "Use /<config>/manifest.json"}

@app.get("/{config}/manifest.json")
async def manifest(config: str):
    try:
        cfg = _b64url_decode(config)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid config encoding")

    service = cfg.get("service", "unknown")
    # Manifest minim Stremio
    return {
        "id": f"community.torrenthan.{service}",
        "version": "0.0.1",
        "name": f"Torrenthan ({service})",
        "description": "Rebuilt addon skeleton (no sources).",
        "resources": ["stream"],
        "types": ["movie", "series"],
        "idPrefixes": ["tt"],
    }

@app.get("/{config}/stream/{type}/{id}.json")
async def stream(config: str, type: str, id: str):
    # aici ar trebui să folosești cfg["service"] + cfg["key"] ca să chemi provider-ul real
    try:
        _ = _b64url_decode(config)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid config encoding")

    return {"streams": []}
