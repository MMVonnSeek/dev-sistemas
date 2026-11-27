from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Plataforma(Base):
    __tablename__ = "plataformas"

    id   = Column(Integer, primary_key=True, index=True)
    nome = Column(String(50), unique=True, nullable=False)

    jogos = relationship("Jogo", back_populates="plataforma")


class Jogo(Base):
    __tablename__ = "jogos"

    id            = Column(Integer, primary_key=True, index=True)
    titulo        = Column(String(100), nullable=False)
    genero        = Column(String(50))
    preco         = Column(Float, nullable=False)
    plataforma_id = Column(Integer, ForeignKey("plataformas.id"), nullable=False)

    plataforma  = relationship("Plataforma", back_populates="jogos")
    avaliacoes  = relationship("Avaliacao", back_populates="jogo")


class Avaliacao(Base):
    __tablename__ = "avaliacoes"

    id         = Column(Integer, primary_key=True, index=True)
    nota       = Column(Integer, nullable=False)
    comentario = Column(String(300))
    jogo_id    = Column(Integer, ForeignKey("jogos.id"), nullable=False)

    jogo = relationship("Jogo", back_populates="avaliacoes")
