from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL do banco - SQLite salva em um arquivo banco.db na pasta do projeto
DATABASE_URL = 'sqlite:///./banco.db'

# Engine: motor de conexão com o banco
engine = create_engine(
    DATABASE_URL,
    connect_args={'check_same_thread': False} # necessário para SQLite
)

# SessionLocal: fábrica de sessões - cada requisição tem a sua própria
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Base: classe base que todos os modelos vão herdar
Base = declarative_base()

# Dependência injetada nos endpoints via Depends(get_db)
# yield entrega a sessão - endpoint executa - finally fecha a sessão
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()