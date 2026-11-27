from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# URL de conexão SQLite -- aponta para o arquivo .db
# O './' significa a pasta raiz do projeto
DB_URL = 'sqlite:///./funcionarios.db'

# Engine: a conexão com o banco
engine = create_engine(
    DB_URL,
    echo=True,              # imprime o SQL no terminal
    connect_args={'check_same_thread': False},  # necessário para SQLite
)

# SessionLocal: fábrica de sessões
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Base: classe pai de todos os modelos ORM
class Base(DeclarativeBase):
    pass