
import os
import gradio as gr
import requests

API_URL = os.getenv("API_URL", "http://127.0.0.1:8000/process")
API_KEY = os.getenv("API_KEY", "")

def demo_clean(text: str) -> str:
    try:
        headers = {}
        if API_KEY:
            headers["x-api-key"] = API_KEY
        resp = requests.post(API_URL, json={"text": text}, headers=headers, timeout=20)
        resp.raise_for_status()
        return resp.json().get("clean_text", "")
    except Exception as e:
        return f"[Error contacting API at {API_URL}: {e}]"

with gr.Blocks(title="Smart Punctuation Fixer") as demo:
    gr.Markdown("# Smart Punctuation & Whitespace Fixer\nPaste messy text on the left, get clean text on the right.")
    with gr.Row():
        inp = gr.Textbox(label="Input text", lines=10, value='Here’s  a   sample— with  odd  spaces.\nLine breaks\r\nand “quotes”.')
        out = gr.Textbox(label="Cleaned text", lines=10)
    btn = gr.Button("Clean")
    btn.click(fn=demo_clean, inputs=inp, outputs=out)

if __name__ == "__main__":
    demo.launch()
