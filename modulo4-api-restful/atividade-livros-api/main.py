from fastapi import FastAPI 
from database import engine, Base 
from router import router as livro_router 
from tags import tags  

Base.metadata.create_all(bind=engine)  

app = FastAPI(  
    title="API de Livros", 
    description=""" 
    # API de Livros 
    Gerencie o acervo de livros com operações completas de CRUD.  
    ### Funcionalidades  - **Listar** livros disponíveis  - **Buscar** livro por ID ou título  - **Cadastrar** novo livro - **Atualizar** dados de um livro  - **Remover** livro do acervo (soft delete)  
    """,  
    version="1.0.0", 
    openapi_tags=tags, 
) 

app.include_router(livro_router) 

@app.get('/')  
def raiz(): 
    return {"status": "online", "docs": "/docs", "versao": "1.0.0"}