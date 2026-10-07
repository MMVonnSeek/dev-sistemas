from app.database import engine, SessionLocal
from app import models
from app.models import Categoria, Fornecedor, Produto

models.Base.metadata.create_all(bind=engine)
print("Tabelas verificadas/criadas no MySQL")

db = SessionLocal()

cat = db.query(Categoria).filter_by(nome="Eletrônicos").first()
if not cat:
    cat = Categoria(nome="Eletrônicos")
    db.add(cat)
    db.commit()
    db.refresh(cat)

forn = db.query(Fornecedor).filter_by(nome="Dell").first()
if not forn:
    forn = Fornecedor(nome="Dell")
    db.add(forn)
    db.commit()
    db.refresh(forn)

prod = Produto(
    nome="Notebook Dell 15",
    preco=3499.90,
    quantidade=10,
    categoria_id=cat.id,
    fornecedor_id=forn.id  # Troque por None para salvar sem fornecedor
)

db.add(prod)
db.commit()

print("Dados inseridos no MySQL com sucesso!")
db.close()