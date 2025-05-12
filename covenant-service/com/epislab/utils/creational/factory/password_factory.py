import smtplib
import string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
import shortuuid
from com.epislab.utils.creational.abstract.abstract_factory import AbstractFactory
from com.epislab.utils.creational.singleton.registry import email_singleton




class CreatePassword:
    password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def __init__(self, password: str):
        self.password = password

    def hash(self) -> str:
        return self.password_context.hash(self.password)

    def verify(self, hashed_password: str) -> bool:
        return self.password_context.verify(self.password, hashed_password)


class PasswordFactory(AbstractFactory):
    def create(self, password: str) -> CreatePassword:
        return CreatePassword(password)


# ✅ 4. UUIDFactory: UUID 및 트랜잭션 번호 객체를 생성하는 팩토리
class CreateUUID:
    def __init__(self, length: int, alphabet: str = string.ascii_lowercase + string.digits):
        self.length = length
        self.alphabet = alphabet
        
    def generate(self) -> str:
         return shortuuid.ShortUUID(alphabet=self.alphabet).random(length=self.length)
    



class UUIDFactory(AbstractFactory):
    def create(self, length: int, alphabet: str = string.ascii_lowercase + string.digits) -> CreateUUID:
        return CreateUUID(length, alphabet)


# ✅ 5. EmailFactory: 이메일 객체를 생성하는 팩토리
class CreateEmail:
    def __init__(self, recipient_email: str, subject: str, body: str):
        self.recipient_email = recipient_email
        self.subject = subject
        self.body = body

    def send(self):
        message = MIMEMultipart()
        message["From"] = email_singleton.smtp_sender_email
        message["To"] = self.recipient_email
        message["Subject"] = self.subject
        message.attach(MIMEText(self.body, _subtype="html"))

        with smtplib.SMTP_SSL(host=email_singleton.smtp_host, port=465) as server:
            server.login(email_singleton.smtp_sender_email, email_singleton.smtp_sender_password)
            server.sendmail(email_singleton.smtp_sender_email, self.recipient_email, message.as_string())


class EmailFactory(AbstractFactory):
    def create(self, recipient_email: str, subject: str, body: str) -> CreateEmail:
        return CreateEmail(recipient_email, subject, body)


# ✅ OAuth2 토큰 인증
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token", auto_error=False)


# ✅ 사용 예시
if __name__ == "__main__":
    # TokenFactory 사용

    # PasswordFactory 사용
    password_factory = PasswordFactory()
    password = password_factory.create("secure_password")
    hashed_password = password.hash()
    print(f"Hashed Password: {hashed_password}")
    print(f"Verify Password: {password.verify(hashed_password)}")