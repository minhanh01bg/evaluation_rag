import toml

import logging

class Config:
    toml_settings = toml.load("../settings.toml")
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

    # goole
    GOOGLE_API_KEY = toml_settings['google']['GOOGLE_API_KEY']
    GOOGLE_CLIENT_ID = toml_settings['google']['GOOGLE_CLIENT_ID']
    GOOGLE_CLIENT_SECRET = toml_settings['google']['GOOGLE_CLIENT_SECRET']
    SECRET_KEY = toml_settings['auth']['SECRET_KEY']

    # aws
    S3_BUCKET_NAME = toml_settings['s3']['S3_BUCKET_NAME']
    AWS_ACCESS_KEY = toml_settings['s3']['AWS_ACCESS_KEY']
    AWS_SECRET_KEY = toml_settings['s3']['AWS_SECRET_KEY']
    REGION_NAME = toml_settings['s3']['REGION_NAME']
    DISTRIBUTION_DOMAIN_NAME = toml_settings['s3']['DISTRIBUTION_DOMAIN_NAME']

    # langsmith
    LANGSMITH_TRACING = toml_settings['langsmith']['LANGSMITH_TRACING']
    LANGSMITH_ENDPOINT = toml_settings['langsmith']['LANGSMITH_ENDPOINT']
    LANGSMITH_API_KEY = toml_settings['langsmith']['LANGSMITH_API_KEY']
    LANGSMITH_PROJECT = toml_settings['langsmith']['LANGSMITH_PROJECT']
    
    # url
    LIMIT = toml_settings['url']['LIMIT']

    # email
    MAIL_USERNAME=toml_settings['email']['MAIL_USERNAME']
    MAIL_PASSWORD=toml_settings['email']['MAIL_PASSWORD']
    MAIL_SERVER=toml_settings['email']['MAIL_SERVER']
    MAIL_PORT=toml_settings['email']['MAIL_PORT']
    MAIL_FROM=toml_settings['email']['MAIL_FROM']
    MAIL_FROM_NAME=toml_settings['email']['MAIL_FROM_NAME']
    MAIL_STARTTLS=toml_settings['email']['MAIL_STARTTLS']
    MAIL_SSL_TLS=toml_settings['email']['MAIL_SSL_TLS']
    USE_CREDENTIALS=toml_settings['email']['USE_CREDENTIALS']
    VALIDATE_CERTS=toml_settings['email']['VALIDATE_CERTS']

    # paypal
    PAYPAL_API_BASE = toml_settings['paypal']['PAYPAL_API_BASE']
    PAYPAL_CLIENT_ID = toml_settings['paypal']['PAYPAL_CLIENT_ID']
    PAYPAL_CLIENT_SECRET = toml_settings['paypal']['PAYPAL_CLIENT_SECRET']
    BRAND_NAME = toml_settings['paypal']['BRAND_NAME']
    
    # frontend
    FRONTEND_URL = toml_settings['frondend']['FRONTEND_URL']

configs = Config()

from starlette.config import Config

config_data = {
    'GOOGLE_CLIENT_ID': configs.GOOGLE_CLIENT_ID,
    'GOOGLE_CLIENT_SECRET': configs.GOOGLE_CLIENT_SECRET,
    'SECRET_KEY': configs.SECRET_KEY,
}

config_goole = Config(environ=config_data)