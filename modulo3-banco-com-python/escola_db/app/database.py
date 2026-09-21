from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import create_engine
DB_URL = 'sqlite:///./escola.db'
engine = create_engine(DB_URL, echo=True, connect_args={'check_same_thread': False})
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
class Base(DeclarativeBase):
    pass

