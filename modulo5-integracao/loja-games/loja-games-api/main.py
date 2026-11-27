from fastapi import FastAPI
from database import engine, Base
from tags import tags
from routers import plataformas, jogos, avaliacoes
from fastapi.middleware.cors import CORSMiddleware

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

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(plataformas.router)
app.include_router(jogos.router)
app.include_router(avaliacoes.router)

@app.get("/")
def raiz():
    return {"status": "online", "docs": "/docs", "versao": "1.0.0"}
