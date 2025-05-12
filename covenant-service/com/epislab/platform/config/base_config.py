from pydantic import BaseModel

class BaseConfig(BaseModel):
    """공통 설정을 위한 베이스 클래스"""

    class Config:
        
        arbitrary_types_allowed = True
        model_config = {
        "from_attributes": True  # ✅ Pydantic v2 스타일 적용
    }