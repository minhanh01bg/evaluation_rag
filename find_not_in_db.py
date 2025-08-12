import asyncio
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional
import datetime
from app.config import configs
from tqdm.auto import tqdm
import datasets
from push_data import call_add_document_by_texts
# Kết nối MongoDB
import time
MONGODB_URL = configs.MONGO_URL
client = AsyncIOMotorClient(MONGODB_URL)
db = client[configs.MONGO_DB]
documents_collection = db["documents"]

async def find_missing_titles():
    # Load dataset
    ds = datasets.load_dataset("m-ric/huggingface_doc", split="train")

    # Lấy tất cả title đã có trong DB
    existing_titles_cursor = documents_collection.find({}, {"title": 1, "_id": 0})
    existing_titles = {doc["title"] async for doc in existing_titles_cursor}

    # Lọc những title chưa có
    missing_titles = [doc for doc in tqdm(ds) if doc.get("source") not in existing_titles]

    print(f"Số title chưa có: {len(missing_titles)}")
    for i, d in enumerate(missing_titles):  # in thử 20 cái đầu
        print(d['source'])
        call_add_document_by_texts(d["text"], d["source"])
        time.sleep(0.5) 
        # if i == 0: break

    return missing_titles

if __name__ == "__main__":
    asyncio.run(find_missing_titles())
