from app.database import engine, Base
from app import models # importar para registrar os modelos na Base
from app.seed import popular_banco

# create_all: cria as tabelas que não existem ainda
# Se a tabela já existe: não apaga, não muda nada
Base.metadata.create_all(bind=engine)
popular_banco()
print('Pronto')