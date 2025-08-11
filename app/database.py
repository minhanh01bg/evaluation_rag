from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional
import datetime
from config import configs
# Kết nối tới MongoDB
MONGODB_URL = configs.MONGO_URL
client = AsyncIOMotorClient(MONGODB_URL)
db = client[configs.MONGO_DB]  # your name of database


# evaluation
evaluation_collection = db['evaluation']