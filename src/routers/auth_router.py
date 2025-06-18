from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.schemas.auth import LoginRequest, TokenResponse
from src.services.auth_service import authenticate
from src.common.dependencies import get_db

router = APIRouter()


@router.post("/login", response_model=TokenResponse)
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    token = authenticate(db, payload.tipo_doc, payload.documento, payload.password)
    return {"access_token": token}
