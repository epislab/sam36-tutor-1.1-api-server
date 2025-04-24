from pydantic import BaseModel, EmailStr

class UserSchema(BaseModel):
    user_id: str | None = None
    email: EmailStr
    password: str
    name: str
   
    model_config = {
        "from_attributes": True  # ✅ Pydantic v2 스타일 적용
    }

class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str
   
    model_config = {
        "from_attributes": True 
    }