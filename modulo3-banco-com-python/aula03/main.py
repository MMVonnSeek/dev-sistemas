from app.database import engine, Base, SessionLocal
from app import models # importar para registrar os modelos na Base
from app.seed import popular_banco
from app.crud import criar_funcionario

# create_all: cria as tabelas que não existem ainda
# Se a tabela já existe: não apaga, não muda nada
Base.metadata.create_all(bind=engine)
popular_banco()
# 1 CREATE
db = SessionLocal()
try:
    novo = criar_funcionario(db, 'Pedro Alves', 'pedro@empresa.com', 3200.0)
    print(f'Criado: {novo}')
finally:
    db.close()