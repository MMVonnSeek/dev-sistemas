from app.database import engine, SessionLocal, Base
from app import models
from app.crud import inserir_tutor, inserir_animal, inserir_atendimento

# Cria todas as tabelas (na ordem correta — SQLAlchemy resolve as FKs)
Base.metadata.create_all(bind=engine)

def main():
    db = SessionLocal()

    try:
        # Tutores
        t1 = inserir_tutor(db, "Max Muller", "(61) 98888-1111", "max@email.com")
        t2 = inserir_tutor(db, "Alanna", "(61) 97777-2222", "alanna@email.com")
        t3 = inserir_tutor(db, "Sandra", "(61) 96666-3333", "sandra@email.com")

        print(f"Tutores cadastrados: {t1.nome_completo}, {t2.nome_completo}, {t3.nome_completo}")

        # Animais
        a1 = inserir_animal(db, "Ted", "Cachorro", "Labrador", 32.5, t1.id)
        a2 = inserir_animal(db, "Tom", "Gato", "Persa", 4.2, t2.id)
        a3 = inserir_animal(db, "Bolinha","Cachorro", "SRD", 8.0, t1.id)
        a4 = inserir_animal(db, "Nina", "Gato", "Siamês", 3.8, t3.id)
        a5 = inserir_animal(db, "Freddie", "Cachorro", "Golden", 28.0, t2.id)

        print(f"Animais cadastrados: {a1.nome_animal}, {a2.nome_animal}, {a3.nome_animal}, "
              f"{a4.nome_animal}, {a5.nome_animal}")

        # Atendimentos
        at1 = inserir_atendimento(db, "01/10/2025", "Consulta de rotina", 150.00, a1.id)
        at2 = inserir_atendimento(db, "02/10/2025", "Vacina antirrábica", 80.00, a2.id)
        at3 = inserir_atendimento(db, "03/10/2025", "Banho e tosa", 60.00, a3.id)
        at4 = inserir_atendimento(db, "04/10/2025", "Exame de sangue", 120.00, a4.id)
        at5 = inserir_atendimento(db, "05/10/2025", "Castração", 350.00, a5.id)
        at6 = inserir_atendimento(db, "06/10/2025", "Retorno pós-cirúrgico", 80.00, a5.id)
        at7 = inserir_atendimento(db, "07/10/2025", "Consulta — problema de pele", 150.00, a1.id)

        print(f"Atendimentos registrados: {at1.id}, {at2.id}, {at3.id}, "
              f"{at4.id}, {at5.id}, {at6.id}, {at7.id}")

        print("\nBanco populado com sucesso! Arquivo: clinica_vetpet.db")

    finally:
        db.close()


if __name__ == "__main__":
    main()