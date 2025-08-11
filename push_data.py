from tqdm.auto import tqdm
import datasets
from app.config import configs
from uuid import uuid4
import httpx
from huggingface_hub import login
from datetime import datetime, timezone
import time

login(token="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")

API_URL = "http://localhost:8001/api/v1/add_document_by_texts"
BEARER_TOKEN = configs.SITE_KEY

def call_add_document_by_texts(text: str, title: str):
    payload = [
        {
            "text": text,
            "title": title,
            "doc_type": "pdf",
            "object_id": str(uuid4()),
            "updated_time": datetime.now(timezone.utc).isoformat()
        }
    ]
    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}",
        "Content-Type": "application/json"
    }
    try:
        httpx.post(API_URL, json=payload, headers=headers, timeout=5.0)  # timeout nhỏ vì không cần kết quả
    except httpx.RequestError:
        pass  # bỏ qua lỗi vì không cần kết quả

ds = datasets.load_dataset("m-ric/huggingface_doc", split="train")

for i, doc in enumerate(tqdm(ds)):
    call_add_document_by_texts(doc["text"], doc["source"])
    time.sleep(0.5)  # delay tránh spam server
    # if i == 9:
    #     break
