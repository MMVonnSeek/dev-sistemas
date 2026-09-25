from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base
class Curso(Base):
    __tablename__ = 'cursos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    duracao = Column(Integer, nullable=False)
    ativo = Column(Boolean, default=True)
    def __repr__(self): 
        return f'<Curso id={self.id} nome={self.nome}>'

class Aluno(Base):
    __tablename__ = 'alunos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(150), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    matricula = Column(String(20), nullable=False, unique=True)
    ativo = Column(Boolean, default=True)
    def __repr__(self): 
        return f'<Aluno id={self.id} nome={self.nome}>'
