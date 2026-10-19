from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from database import get_db
from models import Livro
from schemas import LivroCreate, LivroPatch, LivroResponse

router = APIRouter(prefix='/livros', tags=['Livros'])

@router.get('/', response_model=List[LivroResponse])
def listar(db: Session = Depends(get_db)):
    return db.query(Livro).filter(Livro.disponivel == True).all()

@router.get('/{livro_id}', response_model=LivroResponse)
def buscar(livro_id: int, db: Session = Depends(get_db)):
    livro = db.query(Livro).filter(Livro.id == livro_id).first()
    if not livro: raise HTTPException(404, 'Livro não encontrado')
    return livro

@router.post('/', response_model=LivroResponse, status_code=201)
def criar(dados: LivroCreate, db: Session = Depends(get_db)):
    livro = Livro(**dados.model_dump())
    db.add(livro); db.commit(); db.refresh(livro)
    return livro

@router.patch('/{livro_id}', response_model=LivroResponse)
def atualizar(livro_id: int, dados: LivroPatch, db: Session = Depends(get_db)):
    livro = db.query(Livro).filter(Livro.id == livro_id).first()
    if not livro: raise HTTPException(404, 'Livro não encontrado')
    for campo, valor in dados.model_dump(exclude_none=True).items():
        setattr(livro, campo, valor)
    db.commit(); db.refresh(livro)
    return livro

@router.delete('/{livro_id}')
def remover(livro_id: int, db: Session = Depends(get_db)):
    livro = db.query(Livro).filter(Livro.id == livro_id).first()
    if not livro: raise HTTPException(404, 'Livro não encontrado')
    livro.disponivel = False
    db.commit()
    return {'mensagem': f'Livro {livro_id} removido'}

# Filtro por título
@router.get('/buscar/', response_model=List[LivroResponse])
def buscar_titulo(titulo: str, db: Session = Depends(get_db)):
    return db.query(Livro).filter(Livro.titulo.ilike(f'%{titulo}%')).filter(Livro.disponivel == True).all()