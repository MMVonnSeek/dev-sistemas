from app.database import engine, SessionLocal
from app import models
from app.models import Genero, Autor, Livro

models.Base.metadata.create_all(bind=engine)
print("Tabelas criadas")

db = SessionLocal()

g1 = Genero(nome="Ficção Científica")
g2 = Genero(nome="Romance")
g3 = Genero(nome="Terror")
db.add(g1); db.add(g2); db.add(g3)
db.commit()
db.refresh(g1); db.refresh(g2); db.refresh(g3)

a1 = Autor(nome="Isaac Asimov", nacionalidade="Americano")
a2 = Autor(nome="Machado de Assis", nacionalidade="Brasileiro")
a3 = Autor(nome="Stephen King", nacionalidade="Americano")
db.add(a1); db.add(a2); db.add(a3)
db.commit()
db.refresh(a1); db.refresh(a2); db.refresh(a3)

livros = [
    Livro(titulo="Fundação", ano_publicacao=1951, genero_id=g1.id, autor_id=a1.id),
    Livro(titulo="Eu, Robô", ano_publicacao=1950, genero_id=g1.id, autor_id=a1.id),
    Livro(titulo="Dom Casmurro", ano_publicacao=1899, disponivel=False, genero_id=g2.id, autor_id=a2.id),
    Livro(titulo="Memórias Póstumas", ano_publicacao=1881, genero_id=g2.id, autor_id=a2.id),
    Livro(titulo="O Iluminado", ano_publicacao=1977, genero_id=g3.id, autor_id=a3.id),
]
for l in livros:
    db.add(l)
db.commit()
print(f" {len(livros)} livros inseridos!")

todos = db.query(Livro).all()
for l in todos:
    print(f" [{l.id}] {l.titulo} ({l.ano_publicacao}) | Disponível: {l.disponivel}")

db.close()