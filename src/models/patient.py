from sqlalchemy import Column, Integer, String, Date
from src.config.database import Base


class Patient(Base):
    __tablename__ = "pacientes"  # la tabla real (schema mediclinic)
    __table_args__ = {"schema": "mediclinic"}

    id_pac = Column(Integer, primary_key=True, index=True)
    tipo_doc1 = Column(Integer)  # tipo de documento
    cpf_pac = Column(String(30), index=True)  # nro de doc
    nm_pac = Column(String(100))
    dtnasc_pac = Column(Date)
    sexo_pac = Column(String(1))
    email_pac = Column(String(70))
    senhaweb = Column(String(15))  # contraseña en texto plano
