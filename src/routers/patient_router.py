from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.schemas.patient import PatientCreate, PatientRead, PatientUpdate
from src.services.patient_service import (
    create_patient,
    list_patients,
    get_patient,
    update_patient,
    delete_patient,
)
from src.common.dependencies import get_db, get_current_patient

router = APIRouter(dependencies=[Depends(get_current_patient)])


@router.get("/", response_model=List[PatientRead])
def list_all(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    return list_patients(db, skip, limit)


@router.post("/", response_model=PatientRead)
def create(paciente: PatientCreate, db: Session = Depends(get_db)):
    return create_patient(db, paciente)


@router.get("/{patient_id}", response_model=PatientRead)
def read(patient_id: int, db: Session = Depends(get_db)):
    patient = get_patient(db, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return patient


@router.put("/{patient_id}", response_model=PatientRead)
def update(patient_id: int, data: PatientUpdate, db: Session = Depends(get_db)):
    patient = update_patient(db, patient_id, data)
    if not patient:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return patient


@router.delete("/{patient_id}")
def delete(patient_id: int, db: Session = Depends(get_db)):
    if delete_patient(db, patient_id) is None:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return {"deleted": True}
