from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database import Base

# # Colunas
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    login = Column(String(50), unique=True, nullable=False)
    perfil = Column(String(20), nullable=False)
    senha_hash = Column(String(250), nullable=False)

class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    unidade = Column(String(20), nullable=False)
    quantidade_estoque = Column(Float, nullable=False, default=0.0)


class Movimentacao(Base):
    __tablename__ = "movimentacoes"

    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String(10), nullable=False)
    quantidade = Column(Float, nullable=False)
    observacao = Column(String(300), nullable=True)
    produto_id = Column(Integer, ForeignKey("produtos.id"), nullable=False)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
