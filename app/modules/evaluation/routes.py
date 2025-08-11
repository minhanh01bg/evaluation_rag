from fastapi import APIRouter
from database import evaluation_collection
from pydantic import BaseModel

class Evaluation(BaseModel):
    question: str
    answer: str

evaluation_router = APIRouter()

@evaluation_router.get('/evaluation')
async def get_evaluation():
    evaluations = await evaluation_collection.find().to_list(length=None)
    return evaluations

@evaluation_router.post('/evaluation')
async def create_evaluation(evaluation: Evaluation):
    result = await evaluation_collection.insert_one(evaluation)
    return result.inserted_id

