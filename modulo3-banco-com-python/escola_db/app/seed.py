from app.database import 
from app.models import Curso, 

def popular_banco():
    db = ()
    try:
        if db.query(Curso).count() > 0:
            print('Banco já populado. Pulando...')
            return
        db.([
            (nome='Desenvolvimento de Sistemas', duracao=1200),
            (nome='Informática para Internet',   duracao=1000),
            (nome='Redes de Computadores',       duracao=800),
        ])
        db.add_all([
            (nome='Lucas Mendes',  email='lucas@senai.com',   matricula='2025001'),
            (nome='Fernanda Reis', email='fernanda@senai.com', matricula='2025002'),
            (nome='Rafael Souza',  email='rafael@senai.com',   matricula='2025003'),
            (nome='Camila Torres', email='camila@senai.com',   matricula='2025004'),
        ])
        db.()
        print('Banco populado com sucesso!')
    except Exception as e:
        db.()
        print(f'Erro: {e}')
    finally:
        db.()