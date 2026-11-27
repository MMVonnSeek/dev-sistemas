from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.database import Base

class Genero(Base):
    __tablename__ = "generos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(80), nullable=False, unique=True)

class Autor(Base):
    __tablename__ = "autores"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(120), nullable=False)
    nacionalidade = Column(String(60), nullable=True)

class Livro(Base):
    __tablename__ = "livros"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(200), nullable=False)
    ano_publicacao = Column(Integer, nullable=True)
    disponivel = Column(Boolean, default=True)
    genero_id = Column(Integer, ForeignKey("generos.id"))
    autor_id = Column(Integer, ForeignKey("autores.id"))