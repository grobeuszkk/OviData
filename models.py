
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base
#from sqlalchemy_utils import ChoiceType



db = create_engine("postgresql+psycopg://postgres:310507@localhost:5432/OviData")

base = declarative_base()

class Usuario(base):

    __tablename__ = "usuarios"

    id = Column("id",Integer,nullable=False, primary_key=True, autoincrement=True)
    nome = Column("nome",String, nullable=False)
    email = Column("email",String, nullable=False)
    senha = Column("senha",String, nullable=False)
    status = Column("status",String)
    cargo = Column("cargo",Integer,ForeignKey("funcoes.id"), nullable=False)

    def __init__(self, nome, email, senha, cargo):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cargo = cargo

class Localizacao(base):
    __tablename__ = "localizacao"
    id = Column("id",Integer,nullable=False, primary_key=True, autoincrement=True)
    cep = Column("cep",String, nullable=False)
    rua = Column("rua",String, nullable=False)
    bairro = Column("bairro",String, nullable=False)
    numero = Column("numero",Integer, nullable=False)
    referencia = Column("referencia",String, nullable=True)


    def __init__(self, cep, rua, numero, bairro, referencia):
        self.cep = cep
        self.rua = rua
        self.numero = numero
        self.referencia = referencia
        self.bairro = bairro

class Ovitrampa(base):
    __tablename__ = "ovitrampa"

    id = Column("id",Integer,nullable=False, primary_key=True, autoincrement=True)
    data_coleta = Column("data_coleta",DateTime, nullable=False)
    observacoes = Column("observacoes",String, nullable=True)
    id_localizacao = Column("id_localizacao",Integer, ForeignKey("localizacao.id"), nullable=False)

class Palheta(base):
    __tablename__ = "palheta"
    id = Column("id",Integer,nullable=False, primary_key=True, autoincrement=True)
    imagem = Column("imagem",String, nullable=False)
    qtd_ovos = Column("qtd_ovos",Integer, nullable=False)
    qtd_danificados = Column("qtd_danificados",Integer, nullable=False)
    ovitrampa = Column("Ovitrampa",Integer, ForeignKey("ovitrampa.id"),nullable=False, unique=True)

class Funcoes(base):

    __tablename__ = "funcoes"

 #   CARGOS = (

  #  ("ADMIN", "ADMIN"),
   # ("FUNCIONARIO", "FUNCIONARIO")

    #)

    id = Column("id",Integer,nullable=False, primary_key=True, autoincrement=True)
    cargo = Column("cargo",String, nullable=False)

    def __init__(self, cargo):

        self.cargo = cargo


class Analise(base):
    __tablename__ = "analise"

    id = Column("id",Integer,nullable=False, primary_key=True, autoincrement=True)
    tempo_exec = Column("tempo_exec",Float, nullable=False, default=0)
    confianca = Column("confianca",Float, nullable=False, default=0)
    acuracia = Column("acuracia",Float, nullable=False, default=0)
    ovitrampa = Column("ovitrampa",Integer, ForeignKey("ovitrampa.id"), nullable=False)