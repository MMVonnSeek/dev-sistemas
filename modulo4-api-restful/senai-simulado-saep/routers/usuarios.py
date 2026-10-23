from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional
from database import get_db
from models import Usuario

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

class UsuarioCreate(BaseModel):
    nome: str
    login: str
    perfil: str

class UsuarioUpdate(BaseModel):
    nome: Optional[str] = None
    login: Optional[str] = None
    perfil: Optional[str] = None

def get_or_404(usuario_id: int, db: Session) -> Usuario:
    u = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not u:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return u

@router.get("/")
def listar(db: Session = Depends(get_db)):
    return db.query(Usuario).all()

@router.get("/{usuario_id}")
def buscar(usuario_id: int, db: Session = Depends(get_db)):
    return get_or_404(usuario_id, db)

@router.post("/", status_code=201)
def criar(dados: UsuarioCreate, db: Session = Depends(get_db)):
    existente = db.query(Usuario).filter(Usuario.login == dados.login).first()
    if existente:
        raise HTTPException(status_code=409, detail="Login já cadastrado")
    novo = Usuario(**dados.model_dump())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@router.put("/{usuario_id}")
def atualizar(usuario_id: int, dados: UsuarioUpdate, db: Session = Depends(get_db)):
    u = get_or_404(usuario_id, db)
    if dados.nome is not None: u.nome = dados.nome
    if dados.login is not None: u.login = dados.login
    if dados.perfil is not None: u.perfil = dados.perfil
    db.commit()
    db.refresh(u)
    return u

@router.delete("/{usuario_id}")
def deletar(usuario_id: int, db: Session = Depends(get_db)):
    u = get_or_404(usuario_id, db)
    db.delete(u)
    db.commit()
    return {"mensagem": f"Usuário {usuario_id} removido"}