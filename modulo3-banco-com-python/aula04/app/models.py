# Definir modelo de tabelas
from app.database import Base
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey

class Categoria(Base):
    __tablename__ = "categorias"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(80), nullable=False, unique=True)

class Fornecedor(Base):
    __tablename__ = "fornecedores"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(80), nullable=False)
    contato = Column(String(80), nullable=False)

class Produto(Base):
    __tablename__ = "produtos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(80), nullable=False)
    preco = Column(Float, nullable=False)
    quantidade = Column(Integer, default=0)
    ativo = Column(Boolean, default=True)
    categoria_id = Column(Integer, ForeignKey("categorias.id"))
    fornecedor_id = Column(Integer, ForeignKey("fornecedores.id"))

    