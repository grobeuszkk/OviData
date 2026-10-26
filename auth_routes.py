from fastapi import APIRouter, Depends, HTTPException
from pip._internal.network import auth
from starlette.responses import HTMLResponse

from dependencies import pegar_sessao
from models import Usuario
from sqlalchemy.orm import sessionmaker
from models import db
from main import bcrypt_context
from schemas import UsuarioSchemas
from sqlalchemy.orm import Session
from schemas import LoginSchemas

auth_router = APIRouter(prefix="/auth", tags=["Auth"])

def criar_token(id_usuario):
  token = f"djkhasvbdahsvj{id_usuario}"
  return token


@auth_router.get("/")
async def home():
 """
 rota padrao de autenticação
 """
 return {"message": "Hello World"}

@auth_router.post("/criar_conta")
async def criar_conta(usuario_schema:UsuarioSchemas, session = Depends(pegar_sessao)):

    usuario = session.query(Usuario).filter(Usuario.email == usuario_schema.email).first()
    if usuario:
        raise HTTPException(status_code=400, detail="E-mail do usuário já cadastrado!!")
    else:
        senha_criptografada = bcrypt_context.hash(usuario_schema.senha)
        novo_usuario = Usuario(usuario_schema.nome, usuario_schema.email, senha_criptografada, usuario_schema.cargo)
        session.add(novo_usuario)
        session.commit()
        return{"message": f"Usuario criado com sucesso{usuario_schema.email}"}

@auth_router.post("/login")
async def login(login_schema: LoginSchemas, session: Session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email == login_schema.email).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    else:
        access_token = criar_token(usuario.id)
        return{"access_token": access_token,
               "token_type": "Bearer"
               }