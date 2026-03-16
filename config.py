from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SECRET_KEY=os.getenv("SECRET_KEY")
    ALGORITHM="HS256"
    ACCESS_TOKEN_EXPIRE_SECONDS=60*15
    DEBUG="True"