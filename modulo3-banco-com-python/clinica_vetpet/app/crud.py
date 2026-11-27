from sqlalchemy.orm import Session
from app.models import Tutor, Animal, Atendimento


def inserir_tutor(db: Session, nome_completo: str, telefone: str, email: str) -> Tutor:
    tutor = Tutor(nome_completo=nome_completo, telefone=telefone, email=email)
    db.add(tutor)
    db.commit()
    db.refresh(tutor)
    return tutor


def inserir_animal(
    db: Session,
    nome_animal: str,
    especie: str,
    raca: str,
    peso_kg: float,
    tutor_id: int,
) -> Animal:
    animal = Animal(
        nome_animal=nome_animal,
        especie=especie,
        raca=raca,
        peso_kg=peso_kg,
        tutor_id=tutor_id,
    )
    db.add(animal)
    db.commit()
    db.refresh(animal)
    return animal


def inserir_atendimento(
    db: Session,
    data_atend: str,
    motivo: str,
    valor_cons: float,
    animal_id: int,
) -> Atendimento:
    atendimento = Atendimento(
        data_atend=data_atend,
        motivo=motivo,
        valor_cons=valor_cons,
        animal_id=animal_id,
    )
    db.add(atendimento)
    db.commit()
    db.refresh(atendimento)
    return atendimento