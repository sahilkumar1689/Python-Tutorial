from jose import jwt,JWTError
from datetime import datetime, timedelta
from app.core.config import getenv

# Normally load from env
SECRET_KEY = getenv.JWT_SECRET_KEY
ALGORITHM = getenv.JWT_ALGORITHM


def create_token(data: dict, expires_minutes: int, token_type: str):
    """Generic JWT creator"""
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_minutes or 10)
    to_encode.update({"exp": expire, "type": token_type})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str, expected_type: str):
    """Generic JWT verifier"""
    try:
        print(token,expected_type);
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print("payload2: ",payload);
        if payload.get("type") != expected_type:
            raise JWTError("Invalid token type")
        return payload  # return full payload (contains sub, exp, etc.)
    except JWTError as e:
        print("JWTError:", e) 
        return None

