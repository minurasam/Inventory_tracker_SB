from pydantic import BaseSettings

# This file contains the configuration settings for the FastAPI application.
# It uses Pydantic to manage settings and environment variables.
class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_REGION: str
    S3_BUCKET_NAME: str

    class Config:
        env_file = ".env"

settings = Settings()
