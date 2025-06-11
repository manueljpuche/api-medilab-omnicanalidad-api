# Medilab Omnicanalidad API

API REST desarrollada en **FastAPI** como parte del proyecto de integración de sistemas omnicanal para **Medilab**.

Incluye autenticación basada en grupos de usuario (pacientes, médicos solicitantes, médicos radiólogos) y expone servicios para:

- Gestión de autenticación.
- Consulta de estudios radiológicos.
- Consulta y actualización de citas médicas.

---

## 🚀 Tecnologías utilizadas

- Python 3.10+
- FastAPI
- Uvicorn
- Docker (para despliegue)
- PostgreSQL (base de datos)

---

## 🔐 Autenticación

La API utiliza autenticación mediante **token JWT**, generado tras autenticación por grupo:

- Paciente
- Médico solicitante
- Médico radiólogo

El token debe enviarse en cada request en el header:
```http
Authorization: Bearer <jwt_token>
```

---

## 📚 Endpoints principales

### 🔸 Autenticación

```http
POST /auth/login
```
- **Body**: tipo de usuario, documento, contraseña

### 🔸 Estudios

```http
GET /studies
GET /studies/{study_id}
```

### 🔸 Citas médicas

```http
GET /appointments
PUT /appointments/{appointment_id}
```

---

## 🧪 Entorno de pruebas

Una vez desplegado, el entorno estará disponible en Render con una URL pública.

---

## 👨‍💼 Desarrollador

**Manuel de Jesús Puche Gómez**  
Desarrollador Backend  
📧 mpuche10@gmail.com

🗓️ Fecha: 2025-06-11
