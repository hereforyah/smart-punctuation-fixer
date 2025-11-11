# Smart Punctuation & Whitespace Fixer

Normalize punctuation and whitespace without changing meaning. Great for cleaning text copied from PDFs, OCR output, and messy editors.

## Features
- Converts curly quotes to straight quotes
- Collapses repeated whitespace and odd line breaks
- Light dash rule: " - " → "—"
- Pure functions + FastAPI endpoint
- Gradio demo app

---

## Quickstart (Local)

```bash
# 1) Create and activate a virtualenv (Windows PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# or macOS/Linux
python3 -m venv .venv
source .venv/bin/activate

# 2) Install dependencies
pip install -r requirements.txt

# 3) Run the API
uvicorn app.main:app --reload

# 4) In another terminal, run the demo (optional)
# Set API_URL if your API isn't on localhost:8000
gradio demo/app.py
```

**Test it:**
```bash
curl -s -X POST "http://127.0.0.1:8000/process" \
  -H "Content-Type: application/json" \
  -d "{\"text\": \"Here’s  a   sample— with  odd  spaces.\\nLine breaks\\r\\nand “quotes”.\"}"
```

---

## Deploy to Render (Free Tier)

1. Create a new **Web Service** on Render and connect this repo or upload it.
2. **Build Command:** `pip install -r requirements.txt`
3. **Start Command:** `uvicorn app.main:app --host 0.0.0.0 --port 8000`
4. (Optional) Set `API_KEY` env var to require an API key.

---

## Hugging Face Demo (Free)

- Create a new **Space** (Gradio).
- Upload files from `demo/` and set an env var `API_URL` to your Render URL (e.g., `https://smart-punctuation-fixer.onrender.com/process`).
- (Optional) Add `API_KEY` env var and your app will send it as `x-api-key`.

---

## Testing

```bash
pytest -q
```

---

## API

**POST** `/process`  
Request:
```json
{ "text": "Your raw text here..." }
```
Response:
```json
{ "clean_text": "Cleaned text..." }
```

**GET** `/health` → `{"ok": true, "service": "Smart Punctuation Fixer"}`

---

## Security
If you set `API_KEY` in the environment, requests must include header `x-api-key: <your-key>`.
If unset, the service runs open (demo-friendly).
