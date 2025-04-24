from datetime import UTC, datetime
from sqlalchemy import TIMESTAMP, Column, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ManagerEntity(Base):
    __tablename__ = "manager"

    user_id = Column(String, primary_key=True, doc="개인정보동의내역id")
    personal_id = Column(String, nullable=True)
    survey_id = Column(String, nullable=True)
    member_number = Column(String, nullable=True)
    role = Column(String, nullable=True)
    fullname = Column(String, nullable=True)
    nickname = Column(String, nullable=True)
    gender = Column(String, nullable=True)
    birth_date = Column(String, nullable=True)
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, nullable=True)
    street = Column(String, nullable=True)
    suburb = Column(String, nullable=True)
    postcode = Column(String, nullable=True)
    profile_image = Column(String, nullable=True)
    password = Column(String, nullable=False)
    
    # ✅ `created_at`은 DB에서 자동 생성
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now(), doc="생성 날짜")

    # ✅ `updated_at`은 FastAPI에서 직접 갱신
    updated_at = Column(TIMESTAMP, nullable=False, doc="수정 날짜")
    
    __mapper_args__ = {
        "polymorphic_identity": "manager",
        "polymorphic_on": role  # 역할(role)에 따라 WorkerEntity, SupervisorEntity로 매핑
    }


    def update_timestamp(self):
        """FastAPI에서 `updated_at`을 직접 갱신하는 메서드"""
        self.updated_at = datetime.now(UTC)