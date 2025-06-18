from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi import HTTPException, status
from src.config.settings import settings

ALGORITHM = "HS256"


def create_token(subject: str) -> str:
    exp = datetime.utcnow() + timedelta(minutes=settings.JWT_EXP_MINUTES)
    payload = {"sub": subject, "exp": exp}
    return jwt.encode(payload, settings.JWT_SECRET, algorithm=ALGORITHM)


def verify_token(token: str) -> str:
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[ALGORITHM])
        return payload["sub"]
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token"
        )
