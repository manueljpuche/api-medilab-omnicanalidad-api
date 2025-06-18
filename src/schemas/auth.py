from pydantic import BaseModel


class LoginRequest(BaseModel):
    tipo_doc: int
    documento: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
