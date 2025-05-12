import os
from com.epislab.utils.config.base_config import BaseConfig
class EmailSingleton(BaseConfig):
    """이메일 관련 환경 설정 (싱글톤 패턴 적용)"""

    _instance = None  # ✅ 싱글톤 인스턴스를 저장할 변수

    def __new__(cls):
        """싱글톤 패턴 적용: 인스턴스가 없을 때만 생성"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        """초기화: 환경 변수 로드"""
        self.smtp_sender_email = os.getenv("SMTP_SENDER_EMAIL")
        self.smtp_sender_password = os.getenv("SMTP_SENDER_PASSWORD")
        self.smtp_host = os.getenv("SMTP_HOST")


# ✅ 전역적으로 사용할 싱글톤 인스턴스 생성
email_singleton = EmailSingleton()