from app.database import engine, Base, SessionLocal
from app import models # importar para registrar os modelos na Base
from app.seed import popular_banco
from app.crud import criar_funcionario, listar_funcionarios, buscar_funcionario, atulizar_funcionario, desativar_funcionario
from app.crud import criar_departamento, listar_departamentos, atualizar_departamento, desativar_departamento

# create_all: cria as tabelas que não existem ainda
# Se a tabela já existe: não apaga, não muda nada
Base.metadata.create_all(bind=engine)
popular_banco()
# 1 CREATE
db = SessionLocal()
try:
    novo = criar_funcionario(db, 'Pedro Alves', 'pedro@empresa.com', 3200.0)
    print(f'Criado: {novo}')

# 2 READ
    todos = listar_funcionarios(db)
    print(f'Total: {len(todos)} funcionarios')
    for funcionario in todos:
        print(f' {funcionario.nome} - R${funcionario.salario}')

    um = buscar_funcionario(db, 1)
    if um:
        print(f'\nFuncionário 1: {um.nome}')

# 3 UPDATE
    atualizado = atulizar_funcionario(db, 1, salario=5500.0)
    print(f'{atualizado.nome}: R$ {atualizado.salario}')

# 4 DELETE
    desativado = desativar_funcionario(db, 3)
    print(f'{desativado.nome}: ativo={desativado.ativo}')

    ativo = listar_funcionarios(db, apenas_ativos=True)
    print(f'Ativos restantes: {len(ativo)}')

# Atividade - CRUD de Departamentos 
# Criar
    novo = criar_departamento(db, 'Jurídico', 'JUR')
    print(f'Criado: {novo.nome} ({novo.sigla})')

# Listar
    todos = listar_departamentos(db)
    print(f'Total: {len(todos)} departamentos')

# Atualizar
    atualizado = atualizar_departamento(db, novo.id, 'Jurídico e Compliance')
    print(f'Atualizado: {atualizado.nome}')

# Desativar
    desativado = desativar_departamento(db, novo.id)
    print(f'Desativado: {desativado.nome} -- ativo={desativado.ativo}')
finally:
    db.close()