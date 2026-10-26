from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies import pegar_sessao
from schemas import RequestSchemas
from models import Usuario
request_router = APIRouter(prefix="/requests", tags=["Requests"])

@request_router.get("/")
async def requests():

    return {"message: Acessou os requests"}

