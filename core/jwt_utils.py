import jwt
from config import Config

#encode token 
def encode(payload):
    encoded_jwt=jwt.encode(payload,Config.SECRET_KEY,algorithm=Config.ALGORITHM)
    return encoded_jwt
 
#decode token   
def decode(token):
    try:
        decoded_jwt=jwt.decode(token,Config.SECRET_KEY,Config.ALGORITHM,options={"verify_exp":False}) #süre kontrolü kapalı
        return decoded_jwt        
    except jwt.ExpiredSignatureError:
        return "Token Expired"
    except jwt.InvalidTokenError:
        return "Invalid Token"