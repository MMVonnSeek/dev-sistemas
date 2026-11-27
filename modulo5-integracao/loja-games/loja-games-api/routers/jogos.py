from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional
from database import get_db
from models import Jogo, Plataforma

router = APIRouter(prefix="/jogos", tags=["Jogos"])


class JogoCreate(BaseModel):
    titulo:        str
    genero:        Optional[str] = None
    preco:         float
    plataforma_id: int


class JogoUpdate(BaseModel):
    titulo:        Optional[str]   = None
    genero:        Optional[str]   = None
    preco:         Optional[float] = None
    plataforma_id: Optional[int]   = None


def get_or_404(jogo_id: int, db: Session) -> Jogo:
    j = db.query(Jogo).filter(Jogo.id == jogo_id).first()
    if not j:
        raise HTTPException(status_code=404, detail="Jogo não encontrado")
    return j


@router.get("/", summary="Listar jogos")
def listar(db: Session = Depends(get_db)):
    return db.query(Jogo).all()


@router.get("/{jogo_id}", summary="Buscar jogo por ID",
            responses={404: {"description": "Jogo não encontrado"}})
def buscar(jogo_id: int, db: Session = Depends(get_db)):
    return get_or_404(jogo_id, db)


@router.post("/", status_code=201, summary="Cadastrar jogo",
             responses={404: {"description": "Plataforma não encontrada"}})
def criar(dados: JogoCreate, db: Session = Depends(get_db)):
    plataforma = db.query(Plataforma).filter(Plataforma.id == dados.plataforma_id).first()
    if not plataforma:
        raise HTTPException(status_code=404, detail="Plataforma não encontrada")
    novo = Jogo(**dados.model_dump())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo


@router.put("/{jogo_id}", summary="Atualizar jogo",
            responses={404: {"description": "Jogo ou plataforma não encontrado"}})
def atualizar(jogo_id: int, dados: JogoUpdate, db: Session = Depends(get_db)):
    jogo = get_or_404(jogo_id, db)
    if dados.plataforma_id is not None:
        plat = db.query(Plataforma).filter(Plataforma.id == dados.plataforma_id).first()
        if not plat:
            raise HTTPException(status_code=404, detail="Plataforma não encontrada")
    for campo, valor in dados.model_dump(exclude_none=True).items():
        setattr(jogo, campo, valor)
    db.commit()
    db.refresh(jogo)
    return jogo


@router.delete("/{jogo_id}", summary="Remover jogo",
               responses={404: {"description": "Jogo não encontrado"}})
def deletar(jogo_id: int, db: Session = Depends(get_db)):
    jogo = get_or_404(jogo_id, db)
    db.delete(jogo)
    db.commit()
    return {"mensagem": f"Jogo {jogo_id} removido"}


@router.get("/{jogo_id}/avaliacoes", summary="Listar avaliações de um jogo",
            responses={404: {"description": "Jogo não encontrado"}})
def listar_avaliacoes(jogo_id: int, db: Session = Depends(get_db)):
    jogo = get_or_404(jogo_id, db)
    return jogo.avaliacoes
