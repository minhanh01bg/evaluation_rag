import os
from concurrent.futures import ThreadPoolExecutor
from config import configs
from fastapi import FastAPI, Request, status
from fastapi.staticfiles import StaticFiles
from database import top_questions_collection
from fastapi.middleware.cors import CORSMiddleware
import warnings
from starlette.middleware.sessions import SessionMiddleware
from modules.evaluation.routes import evaluation_router
warnings.filterwarnings('ignore')

app = FastAPI()
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

origins = ["*", ]
os.environ['LANGSMITH_TRACING'] = configs.LANGSMITH_TRACING
os.environ['LANGSMITH_ENDPOINT'] = configs.LANGSMITH_ENDPOINT
os.environ['LANGSMITH_API_KEY'] = configs.LANGSMITH_API_KEY
os.environ['LANGSMITH_PROJECT'] = configs.LANGSMITH_PROJECT

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(SessionMiddleware, secret_key=configs.SECRET_KEY)


app.mount(configs.MEDIA_URL, StaticFiles(directory="alembic"), name="alembic")

app.include_router(router=evaluation_router, prefix=configs.ROUTER, tags=['evaluation_router'])

@app.get('/', status_code=status.HTTP_200_OK, include_in_schema=False)
async def home():
    return {"message": "Server is running!"}


