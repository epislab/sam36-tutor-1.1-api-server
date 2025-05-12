from sqlalchemy import  text          # ✅ SQL 함수만 가져오고

def build_check_user_id_stmt(user_id: str):
    return text("""
        SELECT 1 FROM member
        WHERE user_id = :user_id
        LIMIT 1
    """), {"user_id": user_id}


def build_check_email_stmt(email: str):
    return text("""
        SELECT 1 FROM member
        WHERE email = :email
        LIMIT 1
    """), {"email": email}


def build_login_stmt(email: str, password: str):
    return text("""
        SELECT * FROM member
        WHERE email = :email AND password = :password
        LIMIT 1
    """), {
        "email": email,
        "password": password
    }
