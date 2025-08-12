import asyncio
import httpx
from app.config import configs

API_URL = "http://localhost:8001/api/v1/chat-evaluation"
BEARER_TOKEN = configs.SITE_KEY

async def call_chat_once(payload) -> str:
    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}"
    }
    async with httpx.AsyncClient(timeout=None) as client:
        resp = await client.post(API_URL, json=payload, headers=headers)
        resp.raise_for_status()  # Báo lỗi nếu status != 2xx
        return resp.json()
    

async def call_chat_n_times(n: int, payload) -> list[str]:
    results = []
    for i in range(n):
        result = await call_chat_once(payload)
        results.append(result)
    return results

payload = {
    "question": "Thời tiết hôm nay thế nào?",
    "session_id": "user_test",
    "chat_history": [
    ]
}

# Gọi 1 lần để test
test = asyncio.run(call_chat_once(payload))
print(test)
