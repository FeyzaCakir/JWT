from auth.services import authenticate_user,login_user #kullanıcı kontrol ve token oluşturma
from core.decorators import jwt_required #token çözme
from fastapi import APIRouter,HTTPException,Depends
from auth.schemas import LoginRequest

#Swagger UI (API arayüz) içinde /docs/auth kısmında buradaki uzantılar bulunur 
router=APIRouter(prefix="/auth",tags=["Auth"])


@router.post("/login")
def login(request:LoginRequest):
    try:
        token=login_user(request.email,request.password)
        if not token:
            raise HTTPException(status_code=500,detail="Token generation failed")
        return {"access_token":token, "token_type": "bearer"}
    except Exception as e:
        raise HTTPException(status_code=500,detail=f"Token generation failed: {str(e)}")
        
#token geçerli mi, kullanıcı erişebiliyor mu bilgisi döner
@router.get("/protected")
def protected(user: dict= Depends(jwt_required)):
    return {"message":f"Welcome {user['email']}, this area is protected"}

#veri okuma token içindeki bilgileri çekme
@router.get("/me")
def me(user:dict = Depends(jwt_required)):
    return {"id":user['id'], "email":user['email']}