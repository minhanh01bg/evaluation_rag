import asyncio
import httpx
from app.config import configs

API_URL = "http://localhost:8001/api/v1/chat"
BEARER_TOKEN = configs.SITE_KEY

async def call_chat_once(payload) -> str:
    output = ""
    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}"
    }
    async with httpx.AsyncClient(timeout=None) as client:
        async with client.stream("POST", API_URL, json=payload, headers=headers) as resp:
            async for chunk in resp.aiter_text():
                output += chunk
    return output

async def call_chat_n_times(n: int, payload) -> list[str]:
    results = []
    for i in range(n):
        result = await call_chat_once(payload)
        results.append(result)
    return results

# payload = {
#     "question": "Thời tiết hôm nay thế nào?",
#     "session_id": "user_test",
#     "chat_history": [
#         {"role": "user", "content": "Xin chào"},
#         {"role": "assistant", "content": "Chào bạn"}
#     ]
# }

# # Gọi 1 lần để test
# test = asyncio.run(call_chat_once(payload))
# print(test)
