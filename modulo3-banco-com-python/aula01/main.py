# main.py -- agora usando SQLAlchemy
from sqlalchemy import Column, Integer, String, Boolean, Float, text
from app.database import engine, Base, SessionLocal

# Definir o modelo (tabela) diretamente aqui por enquanto
# Na Aula 14 vai para app/models.py
class Departamento(Base):
    __tablename__ = 'departamentos'
    id    = Column(Integer, primary_key=True, autoincrement=True)
    nome  = Column(String(100), nullable=False)
    sigla = Column(String(10),  nullable=False)
    ativo = Column(Boolean, default=True)

class Cargo(Base):
     __tablename__ = 'cargos'  # nome da tabela

     id = Column(Integer, primary_key=True, autoincrement=True) # tipo inteiro
     titulo = Column(String(100), nullable=False)     # campo obrigatório
     nivel = Column(String(20), nullable=False)
     salario_min = Column(Float, nullable=False)      # número decimal: Float
     salario_max = Column(Float, nullable=False)
     ativo = Column(Boolean, default=True)            # tipo booleano

     def __repr__(self):
         return f'<Cargo ___   nivel={self.nivel}>'    # mostrar o titulo


# Criar a tabela no banco
Base.metadata.create_all(bind=engine)
print('Tabela criada!')

# Inserir dados via sessão
db = SessionLocal()
try:
    # Verificar se já tem dados
    if db.query(Departamento).count() == 0:
        db.add_all([
            Departamento(nome='Tecnologia da Informação', sigla='TI'),
            Departamento(nome='Recursos Humanos', sigla='RH'),
            Departamento(nome='Financeiro', sigla='FIN'),
            Departamento(nome='Comercial', sigla='COM'),
        ])
        db.commit()
        print('Dados inseridos!')

    # Popular cargos (se ainda não tiver dados)
    if db.query(Cargo).count() == 0:       # qual modelo verificar?
        db.add_all([ 
            Cargo(titulo='Desenvolvedor', nivel='Junior', salario_min=2500, salario_max=4000),
            Cargo(titulo='Desenvolvedor', nivel='Pleno', salario_min=4000, salario_max=7000),
            Cargo(titulo='Designer', nivel='Junior', salario_min=2200, salario_max=3500),
            Cargo(titulo='Analista RH', nivel='Pleno', salario_min=3500, salario_max=6000),
        ])
        db.commit()                          # confirmar no banco
    print('Cargos inseridos!')

    # Consultar via SQLAlchemy
    deptos = db.query(Departamento).order_by(Departamento.nome).all()
    print(f'\n{len(deptos)} departamentos no banco:')
    for d in deptos:
        print(f'  {d.id}: {d.nome} ({d.sigla})')

    # SELECT com filtro -- equivalente a WHERE ativo = 1 
    ativos = db.query(Departamento).filter(Departamento.ativo == True).all() 
    print(f'\nDepartamentos ativos: {len(ativos)}') 
 
    # SELECT por sigla específica 
    ti = db.query(Departamento).filter(Departamento.sigla == 'TI').first() 
    print(f'Departamento TI: {ti.nome}') 

    # 1. Listar todos os cargos ordenados por titulo
    todos = db.query(Cargo).order_by(Cargo.titulo).all()  # modelo e campo
    print(f'\n{len(todos)} cargos cadastrados:')
    for c in todos:
        print(f'  {c.titulo} ({c.nivel}) -- R$ {c.salario_min} a R$ {c.salario_max}')

    # 2. Filtrar só cargos Junior
    juniors = db.query(Cargo).filter(Cargo.nivel== 'Junior').all()  # qual campo?
    print(f'\nCargos Junior: {len(juniors)}')

    # 3. Buscar um cargo específico pelo titulo
    designer = db.query(Cargo).filter(Cargo.titulo == 'Designer').first()  # qual título?
    if designer:
        print(f'Designer encontrado: faixa R$ {designer.salario_min} - R$ {designer.salario_max}')

finally:
    db.close()