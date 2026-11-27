from app.database import engine, SessionLocal
from app import models
from app.models import Categoria, Fornecedor, Produto

# Cria as tabelas definidas nos modelos
models.Base.metadata.create_all(bind=engine)
print("Tabelas criadas com sucesso")

db = SessionLocal()

# categorias
cat1 = Categoria(nome="Eletrônicos")
cat2 = Categoria(nome="Roupas")
cat3 = Categoria(nome="Alimentos")

db.add(cat1)
db.add(cat2)
db.add(cat3)
db.commit()
db.refresh(cat1)
db.refresh(cat2)
db.refresh(cat3)
print(f'Categorias criadas: {cat1.id}, {cat2.id}, {cat3.id}')

# fornecedores
forn1 = Fornecedor(nome="Tech LTDA", contato="tech@email.com")
forn2 = Fornecedor(nome="Moda LTDA", contato="moda@email.com")
forn3 = Fornecedor(nome="Alimento LTDA", contato="alimento@email.com")

db.add(forn1)
db.add(forn2)
db.add(forn3)
db.commit()
db.refresh(forn1)
db.refresh(forn2)
db.refresh(forn3)
print(f'Fornecedores criados: {forn1.id}, {forn2.id}, {forn3.id}')

# produtos
produtos = [
    Produto(nome="Notebook Dell 15", preco=3500.0, quantidade=10, 
            categoria_id=cat1.id, fornecedor_id=forn1.id),
    Produto(nome="Mouse", preco=89.90, quantidade=50,
            categoria_id=cat1.id, fornecedor_id=forn1.id),
    Produto(nome="Camisa", preco=50.0, quantidade=80,
            categoria_id=cat2.id, fornecedor_id=forn2.id),
    Produto(nome="Calça", preco=100.0, quantidade=45,
            categoria_id=cat2.id, fornecedor_id=forn2.id),
    Produto(nome="Arroz", preco=29.90, quantidade=200,
            categoria_id=cat3.id, fornecedor_id=forn3.id),
    Produto(nome="Pão", preco=8.90, quantidade=400,
            categoria_id=cat3.id, fornecedor_id=forn3.id),
]
for p in produtos:
    db.add(p)
db.commit()
print(f' {len(produtos)} produtos inseridos')

# Listar pra confirmar
todos = db.query(Produto).all()
print("\n Produtos no banco")
for p in todos:
    print(f' [{p.id}] {p.nome} R$ {p.preco:.2f} Qtd: {p.quantidade}')
db.close()