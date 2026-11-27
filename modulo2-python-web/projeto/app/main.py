from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import tarefas

app = FastAPI(
    title='API de Tarefas - SENAI',
    description='Sistema de gerenciamento de tarefas. Modulo 2',
    version='1.0.0',
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(tarefas.router)

@app.get('/', tags=['Geral'], summary='Status da API')
def raiz():
    return {
        'status':  'online',
        'versao':  '1.0.0',
        'tarefas': f'{len(tarefas.banco)} tarefas cadastradas',
    }