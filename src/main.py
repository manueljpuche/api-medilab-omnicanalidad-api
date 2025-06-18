from fastapi import FastAPI
from src.routers.auth_router import router as auth_router
from src.routers.patient_router import router as patient_router

app = FastAPI(title="Medilab Omnicanalidad API")

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(patient_router, prefix="/patients", tags=["Patients"])
