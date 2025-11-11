
from __future__ import annotations
from pydantic import BaseModel, Field

class Input(BaseModel):
    text: str = Field(..., description="Raw text that may contain curly quotes, odd whitespace, etc.")

class Output(BaseModel):
    clean_text: str = Field(..., description="Normalized and cleaned text.")
