from data.users import find_user_by_email
import bcrypt
from core.jwt_utils import encode
from config import Config
from datetime import timedelta,datetime
from fastapi import HTTPException

def authenticate_user(email,password):
    user=find_user_by_email(email)
    if not user:
        return None
    if not bcrypt.checkpw(password.encode("utf-8"),user.password):
        return None
    
    return user
    
    
def login_user(email,password):
    user=authenticate_user(email,password)
    if not user:
        raise HTTPException(status_code=400,detail="User not found")

    payload={
        "id": user.id,
        "email":user.email,
        "exp":int((datetime.utcnow()+ timedelta(seconds=Config.ACCESS_TOKEN_EXPIRE_SECONDS)).timestamp())
    }
    token=encode(payload)
    return token
   