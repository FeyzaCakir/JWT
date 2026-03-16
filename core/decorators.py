from core.jwt_utils import decode
from fastapi import Request,HTTPException

def jwt_required(request: Request):
    auth_header= request.headers.get("Authorization")
    if not auth_header:
        raise HTTPException(status_code=401,detail="Authorization header missing")

    parts=auth_header.split()
    if len(parts)!=2 or parts[0].lower()!="bearer":
        raise HTTPException(status_code=401,detail="Invalid Authorization format")
    
    token=parts[1]
    decoded_token=decode(token)
    if decoded_token =="Token Expired":
        raise HTTPException(status_code=401,detail="Token Expired")
    if decoded_token=="Invalid Token":
        raise HTTPException(status_code=401,detail="Invalid Token")
    
    return decoded_token