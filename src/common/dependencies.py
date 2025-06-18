from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from src.config.database import SessionLocal
from src.common.jwt import verify_token
from src.models.patient import Patient

security = HTTPBearer()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_patient(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db),
):
    doc_key = verify_token(credentials.credentials)
    patient = (
        db.query(Patient)
        .filter(Patient.cpf_pac == doc_key)  # usamos documento como sub
        .first()
    )
    if not patient:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Patient not found"
        )
    return patient
