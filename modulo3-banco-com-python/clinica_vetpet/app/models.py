from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.database import Base

class Tutor(Base):
    __tablename__ = "tutores"

    id = Column(Integer, primary_key=True, index=True)
    nome_completo = Column(String(100), nullable=False)
    telefone = Column(String(20),  nullable=False)
    email = Column(String(100), unique=True, nullable=False)


class Animal(Base):
    __tablename__ = "animais"

    id = Column(Integer, primary_key=True, index=True)
    nome_animal = Column(String(60), nullable=False)
    especie = Column(String(40), nullable=False)
    raca = Column(String(60), nullable=True)
    peso_kg = Column(Float, nullable=True)
    tutor_id = Column(Integer, ForeignKey("tutores.id"), nullable=False)


class Atendimento(Base):
    __tablename__ = "atendimentos"

    id = Column(Integer, primary_key=True, index=True)
    data_atend = Column(String(10), nullable=False)   # formato: DD/MM/AAAA
    motivo = Column(String(200), nullable=False)
    valor_cons = Column(Float, nullable=False)
    animal_id = Column(Integer, ForeignKey("animais.id"), nullable=False)