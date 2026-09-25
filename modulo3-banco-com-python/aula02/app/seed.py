from app.database import SessionLocal
<<<<<<< HEAD
from app.models import Departamento, Cargo, Funcionario
=======
from app.models import Departamento, Cargo
>>>>>>> d084443bc33379b9f5cd2d19e8ff9f1437f6eed1

def popular_banco():
    db = SessionLocal()   # abrir sessão
    try:
        # Se já tem dados, não inserir de novo
        if db.query(Departamento).count() > 0:
            print('Banco já preenchido. Pulando...')
            return

        db.add_all([
            Departamento(nome='Tecnologia da Informação', sigla='TI'),
            Departamento(nome='Recursos Humanos', sigla='RH'),
            Departamento(nome='Financeiro', sigla='FIN'),
            Departamento(nome='Comercial', sigla='COM'),
        ])

        db.add_all([
            Cargo(titulo='Desenvolvedor', nivel='Junior', salario_min=2500, salario_max=4000),
            Cargo(titulo='Desenvolvedor', nivel='Pleno', salario_min=4000, salario_max=7000),
            Cargo(titulo='Designer', nivel='Junior', salario_min=2200, salario_max=3500),
            Cargo(titulo='Analista RH', nivel='Pleno', salario_min=3500, salario_max=6000),
        ])

<<<<<<< HEAD
        db.add_all([
            Funcionario(nome='Carlos Silva', email='carlos@empresa.com', salario=4500.0),
            Funcionario(nome='Ana Lima', email='ana@empresa.com', salario=3800.0),
            Funcionario(nome='Bruno Costa', email='bruno@empresa.com', salario=5200.0),
            Funcionario(nome='Diana Rocha', email='diana@empresa.com', salario=6100.0),
        ])

        db.commit()     # confirma tudo no banco de uma vez
        print(f'Funcionarios inseridos!')
=======
        db.commit()     # confirma tudo no banco de uma vez
        print('Banco preenchido com sucesso')
>>>>>>> d084443bc33379b9f5cd2d19e8ff9f1437f6eed1

    except Exception as erro:
        db.rollback()   # desfaz tudo se der erro
        print(f'Erro: {erro}')
    finally:
        db.close()      # lembre-se sempre de fechar a sessão
if __name__=='__main__':
    popular_banco()