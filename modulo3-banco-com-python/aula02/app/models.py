from sqlalchemy import Column, Integer, String, Boolean, Float
from app.database import Base

class Departamento(Base):
    __tablename__ = 'departamentos' # nome da tabela no banco

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    sigla = Column(String(10), nullable=False)
    ativo = Column(Boolean, default=True)

    def __repr__(self):
        return f'<Departamento id={self.id} nome={self.nome}>'

class Cargo(Base):
    __tablename__ = 'cargos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(100), nullable=False)
    nivel = Column(String(20), nullable=False)
    salario_min = Column(Float, nullable=False)
    salario_max = Column(Float, nullable=False)
    ativo = Column(Boolean, default=True)

    def __repr__(self):
        return f'<Cargo {self.titulo} {self.nivel}>'