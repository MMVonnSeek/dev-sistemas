from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from typing import Optional
from auth import criar_hash, verificar_senha, criar_token, usuario_logado

app = FastAPI(title='API de Tarefas', version='1.0.0')

# Banco em memória
tarefas = []
usuarios = []
proximo_id_tarefa = 1
proximo_id_usuario = 1

# Schemas
class TarefaCreate(BaseModel):
    titulo: str = Field(..., min_length=2, max_length=200)
    descricao: str = Field(..., max_length=500)

class TarefaPatch(BaseModel):
    titulo: Optional[str]  = Field(None, min_length=2, max_length=200)
    descricao: Optional[str]  = Field(None, max_length=500)
    concluida: Optional[bool] = None

class UsuarioCreate(BaseModel):
    nome: str = Field(..., min_length=2, max_length=100)
    email: str
    senha: str = Field(..., min_length=8)

class LoginRequest(BaseModel):
    email: str
    senha: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = 'bearer'

def achar_tarefa(tarefa_id: int):
    t = next((t for t in tarefas if t['id'] == tarefa_id), None)
    if not t:
        raise HTTPException(status_code=404, detail=f'Tarefa {tarefa_id} não encontrada')
    return t

# ============================
# AUTENTICAÇÃO 
# Rota POST auth/registro
@app.post('/auth/registro', status_code=201)
def registro(dados: UsuarioCreate):
    global proximo_id_usuario
    if any(u['email'] == dados.email for u in usuarios):
        raise HTTPException(409, 'E-mail já cadastrado')
    novo = {
        'id': proximo_id_usuario,
        'nome': dados.nome,
        'email': dados.email,
        'hash_senha': criar_hash(dados.senha),
    }
    usuarios.append(novo)
    proximo_id_usuario += 1
    return {'id': novo['id'], 'nome': novo['nome'], 'email': novo['email']}


# Rota POST auth/login
@app.post('/auth/login', response_model=TokenResponse)
def login(dados: LoginRequest):
    usuario = next((u for u in usuarios if u['email'] == dados.email), None)
    if not usuario or not verificar_senha(dados.senha, usuario['hash_senha']):
        raise HTTPException(401, 'E-mail ou senha incorretos')
    token = criar_token({'sub': usuario['email'], 'nome': usuario['nome']})
    return {'access_token': token, 'token_type': ' bearer'}


# 
@app.get('/tarefas')
def listar(): 
    return tarefas

@app.get('/tarefas/{tarefa_id}')
def buscar(tarefa_id: int): return achar_tarefa(tarefa_id)

@app.post('/tarefas', status_code=201)
def criar(dados: TarefaCreate,
          email: str = Depends(usuario_logado)):
    global proximo_id_tarefa
    nova = {'id': proximo_id_tarefa,
            'titulo': dados.titulo,
            'descricao': dados.descricao,
            'concluida': False}
    tarefas.append(nova)
    proximo_id_tarefa += 1
    return nova

@app.patch('/tarefas/{tarefa_id}')
def atualizar(tarefa_id: int, dados: TarefaPatch, email: str = Depends(usuario_logado)):
    t = achar_tarefa(tarefa_id)
    if dados.titulo    is not None: t['titulo']    = dados.titulo
    if dados.descricao is not None: t['descricao'] = dados.descricao
    if dados.concluida is not None: t['concluida'] = dados.concluida
    return t

@app.delete('/tarefas/{tarefa_id}')
def remover(tarefa_id: int, email: str = Depends(usuario_logado)):
    global tarefas
    achar_tarefa(tarefa_id)
    tarefas = [t for t in tarefas if t['id'] != tarefa_id]
    return {'mensagem': f'Tarefa {tarefa_id} removida'}