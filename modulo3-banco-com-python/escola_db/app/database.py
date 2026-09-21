from sqlalchemy.orm import , DeclarativeBase
DB_URL = ':///./escola.db'
engine = create_engine(DB_URL, echo=True, connect_args={'check_same_thread': False})
SessionLocal = (bind=engine, autocommit=False, autoflush=False)
class Base(DeclarativeBase):
    