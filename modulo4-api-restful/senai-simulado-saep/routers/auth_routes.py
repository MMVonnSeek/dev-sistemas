from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import get_db
from models import Usuario
from auth import hash_senha, verificar_senha, criar_token
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/auth", tags=["Autenticação"])

class CadastroForm(BaseModel):
    nome: str
    login: str
    perfil: str  # Ex. "admin" ou "operador"
    senha: str

class LoginForm(BaseModel):
    login: str
    senha: str

# Rota POST /auth/cadastro
@router.post("/cadastro", status_code=201)
def cadastrar(dados: CadastroForm, db:Session = Depends(get_db)):
    existe = db.query(Usuario).filter(Usuario.login == dados.login).first()
    if existe:
        raise HTTPException(status_code=409, detail="Login já em uso")
    novo = Usuario(
        nome = dados.nome,
        login = dados.login,
        perfil = dados.perfil,
        senha_hash = hash_senha(dados.senha),
    )
    db.add(novo)
    db.commit()
    return {"mensagem": "Usuário criado com Sucesso"}


# Rota POST /auth/login
@router.post("/login")
def login(dados: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.login == dados.username).first()
    if not usuario or not verificar_senha(dados.password, usuario.senha_hash):
        raise HTTPException(status_code=401, detail="Login ou senha inválido")
    token = criar_token({"sub": usuario.login})
    return {"access_token": token, "token_type": "bearer"}













































































