from fastapi import FastAPI
from database import engine, Base
from tags import tags
from routers import plataformas, jogos, avaliacoes

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Loja de Games",
    description="""
## Loja de Games 🎮

API para gerenciamento de catálogo de jogos.

### Funcionalidades
- Cadastrar e listar **plataformas**
- Gerenciar o **catálogo de jogos**
- Registrar e consultar **avaliações**
    """,
    version="1.0.0",
    openapi_tags=tags,
)

app.include_router(plataformas.router)
app.include_router(jogos.router)
app.include_router(avaliacoes.router)

@app.get("/")
def raiz():
    return {"status": "online", "docs": "/docs", "versao": "1.0.0"}
