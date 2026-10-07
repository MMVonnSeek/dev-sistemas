from sqlalchemy.orm import Session
from app.models import Categoria, Fornecedor, Produto

def criar_categoria(db: Session, nome: str):
    cat = Categoria(nome=nome)
    db.add(cat)
    db.commit()
    db.refresh(cat)
    return cat

def criar_fornecedor(db: Session, nome: str, contato: str):
    forn = Fornecedor(nome=nome, contato=contato)
    db.add(forn)
    db.commit()
    db.refresh(forn)
    return forn

def criar_produto(db: Session, nome: str, preco: float,
                  quantidade: int, categoria_id: int, fornecedor_id: int):
    prod = Produto(
        nome=nome,
        preco=preco,
        quantidade=quantidade,
        categoria_id=categoria_id,
        fornecedor_id=fornecedor_id,
    )
    db.add(prod)
    db.commit()
    db.refresh(prod)
    return prod