from app.database import engine, 
from app import 
from app.seed import popular_banco
.metadata._all(bind=engine)
popular_banco()
