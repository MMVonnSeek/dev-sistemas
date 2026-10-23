from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional
from database import get_db
from models import Produto

router = APIRouter(prefix="/produtos", tags=["Produtos"])


class ProdutoCreate(BaseModel):
    nome: str
    unidade: str
    quantidade_estoque: float = 0.0


class ProdutoUpdate(BaseModel):
    nome: Optional[str] = None
    unidade: Optional[str] = None
    quantidade_estoque: Optional[float] = None


def get_or_404(produto_id: int, db: Session) -> Produto:
    p = db.query(Produto).filter(Produto.id == produto_id).first()
    if not p:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return p


@router.get("/")
def listar(db: Session = Depends(get_db)):
    return db.query(Produto).all()


@router.get("/{produto_id}")
def buscar(produto_id: int, db: Session = Depends(get_db)):
    return get_or_404(produto_id, db)


@router.post("/", status_code=201)
def criar(dados: ProdutoCreate, db: Session = Depends(get_db)):
    novo = Produto(**dados.model_dump())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo


@router.put("/{produto_id}")
def atualizar(produto_id: int, dados: ProdutoUpdate, db: Session = Depends(get_db)):
    p = get_or_404(produto_id, db)
    if dados.nome is not None: p.nome = dados.nome
    if dados.unidade is not None: p.unidade = dados.unidade
    if dados.quantidade_estoque is not None: p.quantidade_estoque = dados.quantidade_estoque
    db.commit()
    db.refresh(p)
    return p


@router.delete("/{produto_id}")
def deletar(produto_id: int, db: Session = Depends(get_db)):
    p = get_or_404(produto_id, db)
    db.delete(p)
    db.commit()
    return {"mensagem": f"Produto {produto_id} removido"}
