import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from app.config import configs
from push_data import call_add_document_by_texts
# Kết nối MongoDB
import time
MONGODB_URL = configs.MONGO_URL
client = AsyncIOMotorClient(MONGODB_URL)
db = client[configs.MONGO_DB]
documents_collection = db["documents"]
vector_collection = db["chatbotVectorstores"]

import asyncio

async def delete_vectors_with_missing_doc():
    # Lấy toàn bộ _id từ documents_collection
    existing_doc_ids = {
        str(doc["_id"])
        async for doc in documents_collection.find({}, {"_id": 1})
    }

    # Lấy tất cả vector có doc_id không nằm trong existing_doc_ids
    missing_vectors_cursor = vector_collection.find(
        {"doc_id": {"$nin": list(existing_doc_ids)}},
        {"_id": 1, "doc_id": 1}
    )

    # Xóa từng vector
    delete_count = 0
    async for vector in missing_vectors_cursor:
        await vector_collection.delete_one({"_id": vector["_id"]})
        delete_count += 1

    print(f"Đã xóa {delete_count} vectors có doc_id không tồn tại trong documents_collection")

if __name__ == "__main__":
    asyncio.run(delete_vectors_with_missing_doc())