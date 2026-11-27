from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from database import get_db
from models import Avaliacao, Jogo

router = APIRouter(prefix="/avaliacoes", tags=["Avaliacoes"])


class AvaliacaoCreate(BaseModel):
    nota:       int = Field(..., ge=1, le=5)
    comentario: str
    jogo_id:    int


@router.post("/", status_code=201, summary="Registrar avaliação",
             responses={
                 201: {"description": "Avaliação registrada"},
                 404: {"description": "Jogo não encontrado"},
             })
def criar(dados: AvaliacaoCreate, db: Session = Depends(get_db)):
    jogo = db.query(Jogo).filter(Jogo.id == dados.jogo_id).first()
    if not jogo:
        raise HTTPException(status_code=404, detail="Jogo não encontrado")
    nova = Avaliacao(**dados.model_dump())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova


@router.delete("/{avaliacao_id}", summary="Remover avaliação",
               responses={404: {"description": "Avaliação não encontrada"}})
def deletar(avaliacao_id: int, db: Session = Depends(get_db)):
    av = db.query(Avaliacao).filter(Avaliacao.id == avaliacao_id).first()
    if not av:
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")
    db.delete(av)
    db.commit()
    return {"mensagem": f"Avaliação {avaliacao_id} removida"}
