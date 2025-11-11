
from __future__ import annotations
import os
from fastapi import FastAPI, Header, HTTPException
from .schemas import Input, Output
from .logic import clean_text

APP_NAME = "Smart Punctuation Fixer"
API_KEY_ENV = "API_KEY"

app = FastAPI(
    title=APP_NAME,
    version="1.0.0",
    description="Normalize punctuation and whitespace in plain text."
)

def verify_api_key(x_api_key: str | None):
    expected = os.getenv(API_KEY_ENV, "").strip()
    if expected and x_api_key != expected:
        raise HTTPException(status_code=401, detail="Invalid API key")

@app.get("/health")
def health():
    return {"ok": True, "service": APP_NAME}

@app.post("/process", response_model=Output)
def process(payload: Input, x_api_key: str | None = Header(default=None)):
    # Optional API key check; if API_KEY is unset, run open for demos
    if os.getenv(API_KEY_ENV):
        verify_api_key(x_api_key)
    cleaned = clean_text(payload.text)
    return Output(clean_text=cleaned)
