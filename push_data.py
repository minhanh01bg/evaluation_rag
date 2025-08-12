from tqdm.auto import tqdm
import datasets
from app.config import configs
from uuid import uuid4
import logging
import httpx

logger = logging.getLogger(__name__)
from huggingface_hub import login
from datetime import datetime, timezone
import time

login(token=configs.HF_TOKEN)

API_URL = "http://localhost:8001/api/v1/add_document_by_texts"
BEARER_TOKEN = configs.SITE_KEY

def call_add_document_by_texts(text: str, title: str):
    payload = [{
        "text": text,
        "title": title,
        "doc_type": "pdf",
        "object_id": str(uuid4()),
        "updated_time": datetime.now(timezone.utc).isoformat()
    }]
    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}",
        "Content-Type": "application/json"
    }
    try:
        resp = httpx.post(API_URL, json=payload, headers=headers, timeout=5.0)
        resp.raise_for_status()
    except httpx.HTTPStatusError as exc:
        # HTTP errors like 4xx or 5xx
        try:
            detail = exc.response.json().get("detail", {})
        except ValueError:
            detail = exc.response.text
        if exc.response.status_code == 400 and isinstance(detail, dict) and detail.get("message") == "Title exist":
            return  # Bỏ qua lỗi "Title exist"
        logger.warning(f"HTTPStatusError for title={title}: {detail}")
    except httpx.RequestError as exc:
        # Các lỗi như timeout, network, etc.
        logger.error(f"Request failed for title={title}: {str(exc)}")

# ds = datasets.load_dataset("m-ric/huggingface_doc", split="train")

# for i, doc in enumerate(tqdm(ds)):
#     call_add_document_by_texts(doc["text"], doc["source"])
#     time.sleep(0.5)  # delay tránh spam server
#     # if i == 9:
#     #     break
