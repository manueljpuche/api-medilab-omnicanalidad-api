from pydantic import BaseModel, EmailStr, Field
from datetime import date


class PatientBase(BaseModel):
    tipo_doc: int
    documento: str = Field(..., alias="cpf_pac")
    nombre: str = Field(..., alias="nm_pac")
    fecha_nacimiento: date | None = Field(None, alias="dtnasc_pac")
    sexo: str | None = Field(None, alias="sexo_pac")
    email: EmailStr | None = Field(None, alias="email_pac")

    class Config:
        from_attributes = True
        validate_by_name = True


class PatientCreate(PatientBase):
    password: str = Field(..., alias="senhaweb")


class PatientRead(PatientBase):
    id_pac: int


class PatientUpdate(PatientBase):
    password: str | None = Field(None, alias="senhaweb")
