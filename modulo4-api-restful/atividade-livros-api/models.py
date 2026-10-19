from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from database import Base

class Livro(Base):
    __tablename__ = 'livros'
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(200), nullable=False)
    autor = Column(String(150), nullable=False)
    ano_publicacao = Column(Integer, nullable=True)
    disponivel = Column(Boolean, default=True)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())