from pydantic_settings import BaseSettings;
from dotenv import load_dotenv,find_dotenv;

load_dotenv(find_dotenv());


class Settings(BaseSettings):
    DATABASE_URI: str
    JWT_SECRET_KEY :str
    JWT_ALGORITHM :str
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES :int
    MAIL_USER:str
    MAIL_PASS:str
    CLOUDINARY_CLOUD_NAME:str
    CLOUDINARY_API_KEY:str
    CLOUDINARY_API_SECRET:str
        
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


getenv = Settings()

