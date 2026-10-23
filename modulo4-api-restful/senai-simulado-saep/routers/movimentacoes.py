from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional
from database import get_db
from models import Movimentacao, Produto, Usuario

router = APIRouter(prefix="/movimentacoes", tags=["Movimentacoes"])


class MovimentacaoCreate(BaseModel):
    tipo: str
    quantidade: float
    observacao: Optional[str] = None
    produto_id: int
    usuario_id: int


@router.get("/")
def listar(db: Session = Depends(get_db)):
    return db.query(Movimentacao).all()


@router.get("/{movimentacao_id}")
def buscar(movimentacao_id: int, db: Session = Depends(get_db)):
    m = db.query(Movimentacao).filter(Movimentacao.id == movimentacao_id).first()
    if not m:
        raise HTTPException(status_code=404, detail="Movimentação não encontrada")
    return m


@router.post("/", status_code=201)
def criar(dados: MovimentacaoCreate, db: Session = Depends(get_db)):
    # Valida produto
    produto = db.query(Produto).filter(Produto.id == dados.produto_id).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    # Valida usuário
    usuario = db.query(Usuario).filter(Usuario.id == dados.usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")








    # DESAFIO: verifica estoque para saída
    if dados.tipo == "saida":
        if produto.quantidade_estoque < dados.quantidade:
            raise HTTPException(status_code=400, detail="Estoque insuficiente")

    nova = Movimentacao(**dados.model_dump())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova
