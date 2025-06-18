from sqlalchemy.orm import Session
from src.models.patient import Patient
from src.schemas.patient import PatientCreate, PatientUpdate


def create_patient(db: Session, data: PatientCreate) -> Patient:
    patient = Patient(
        tipo_doc1=data.tipo_doc,
        cpf_pac=data.documento,
        nm_pac=data.nombre,
        dtnasc_pac=data.fecha_nacimiento,
        sexo_pac=data.sexo,
        email_pac=data.email,
        senhaweb=data.password,
    )
    db.add(patient)
    db.commit()
    db.refresh(patient)
    return patient


def list_patients(db: Session, skip: int = 0, limit: int = 20):
    return db.query(Patient).offset(skip).limit(limit).all()


def get_patient(db: Session, patient_id: int):
    return db.query(Patient).filter(Patient.id_pac == patient_id).first()


def update_patient(db: Session, patient_id: int, data: PatientUpdate):
    patient = get_patient(db, patient_id)
    if not patient:
        return None
    for field, value in data.dict(exclude_unset=True).items():
        setattr(patient, field, value)
    db.commit()
    db.refresh(patient)
    return patient


def delete_patient(db: Session, patient_id: int):
    patient = get_patient(db, patient_id)
    if not patient:
        return None
    db.delete(patient)
    db.commit()
    return patient
