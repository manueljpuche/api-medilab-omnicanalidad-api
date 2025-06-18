from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from src.models.patient import Patient
from src.common.jwt import create_token


def authenticate(db: Session, tipo_doc: int, documento: str, password: str):
    pac = (
        db.query(Patient)
        .filter(Patient.tipo_doc1 == tipo_doc, Patient.cpf_pac == documento)
        .first()
    )
    if not pac or pac.senhaweb != password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales inválidas"
        )
    return create_token(pac.cpf_pac)
