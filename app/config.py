import toml

import logging

class Config:
    toml_settings = toml.load("./settings.toml")
    # print(config)

    check = True
    ROUTER = '/api/v1' if check == True else ''
    #  DB
    SQLALCHEMY_DATABASE_URL = "sqlite:///./db.sqlite3"
    # SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost/fancy"
    #
    MEDIA_URL = "/alembic"

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("app.log"),  # Ghi log vào file
            logging.StreamHandler()  # Hiển thị log trong console
        ]
    )

    logger = logging.getLogger(__name__)

    OPENAI_API_KEY = toml_settings['openai']['OPENAI_API_KEY']
    MONGO_URL = toml_settings['mongo']['MONGO_URL']
    MONGO_DB = toml_settings['mongo']['MONGO_DB']

    # site
    SITE_KEY = toml_settings['site']['SITE_KEY']

    HF_TOKEN = toml_settings['hf']['HF_TOKEN']


configs = Config()
