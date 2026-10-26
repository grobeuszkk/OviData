#pydantic força a tipagem de dados
from pydantic import BaseModel
from typing import Optional

class UsuarioSchemas(BaseModel):
    nome: str
    email: str
    senha: str
    cargo: int
    status: Optional[bool]
    class Config:
        from_attributes = True

class RequestSchemas(BaseModel):
    usuario: UsuarioSchemas
    class Config:
        from_attributes = True

class LoginSchemas(BaseModel):
    email: str
    senha: str

    class Config:
        from_attributes = True