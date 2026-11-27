from sqlalchemy import Column, String, Integer, Float, Boolean, DateTime
from sqlalchemy.sql import func
from database import Base  # importa a base que criamos no database.py

class Produto(Base):
    __tablename__ = 'produtos' # nome da tabela no banco

    # Colunas da tabela
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    preco = Column(Float, nullable=False)
    estoque = Column(Integer, default=0)
    ativo = Column(Boolean, default=True)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())

    # __repr__ - como o objeto aparece no terminal (útil para debug)
    def __repr__(self):
        return f'<Produto id={self.id} nome={self.nome}>'