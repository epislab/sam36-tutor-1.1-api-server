from pydantic import BaseModel

class BaseConfig(BaseModel):
    """공통 설정을 위한 베이스 클래스"""

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True