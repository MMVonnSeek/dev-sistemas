from app.database import SessionLocal
from app.models import Departamento, Cargo

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

        db.commit()     # confirma tudo no banco de uma vez
        print('Banco preenchido com sucesso')

    except Exception as erro:
        db.rollback()   # desfaz tudo se der erro
        print(f'Erro: {erro}')
    finally:
        db.close()      # lembre-se sempre de fechar a sessão
if __name__=='__main__':
    popular_banco()