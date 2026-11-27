from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from database import engine, Base, get_db
from models   import Usuario
from schemas  import UsuarioCreate, UsuarioPatch, UsuarioResponse, ErroResponse

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='API de Usuários',
    description='Demonstração de validação avançada com Pydantic',
    version='1.0.0'
)
# POST /usuarios ── Cadastrar novo usuário
# response_model=UsuarioResponse garante que a senha NUNCA vai
# aparecer na resposta, mesmo que o objeto Usuario tenha hash_senha.
@app.post('/usuarios',
          response_model=UsuarioResponse,
          status_code=201,
          responses={409: {'model': ErroResponse}})
def criar_usuario(dados: UsuarioCreate, db: Session = Depends(get_db)):
    # Verifica email duplicado antes de tentar inserir
    existe = db.query(Usuario).filter(Usuario.email == dados.email).first()
    if existe:
        raise HTTPException(
            status_code=409,
            detail='E-mail já cadastrado'
        )
    # Em produção: hash_senha = bcrypt.hashpw(dados.senha...)
    # Por enquanto guardamos a senha diretamente só para estudar o schema
    # (no Capítulo 6 implementamos o bcrypt de verdade)
    usuario = Usuario(
        nome = dados.nome,
        email = dados.email,
        hash_senha = dados.senha,  # ← substituir por hash na aula 6
    )
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario   # FastAPI filtra pela UsuarioResponse — sem senha!


# GET /usuarios ── Listar todos
@app.get('/usuarios', response_model=List[UsuarioResponse])
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(Usuario).filter(Usuario.ativo == True).all()


# GET /usuarios/{id} ── Buscar por ID
@app.get('/usuarios/{usuario_id}', response_model=UsuarioResponse)
def buscar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario or not usuario.ativo:
        raise HTTPException(status_code=404, detail='Usuário não encontrado')
    return usuario


# PATCH /usuarios/{id} ── Atualizar parcialmente
@app.patch('/usuarios/{usuario_id}', response_model=UsuarioResponse)
def atualizar_usuario(usuario_id: int, dados: UsuarioPatch,
                       db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario or not usuario.ativo:
        raise HTTPException(status_code=404, detail='Usuário não encontrado')

    # Verifica email duplicado se o cliente quiser mudar o email
    if dados.email and dados.email != usuario.email:
        if db.query(Usuario).filter(Usuario.email == dados.email).first():
            raise HTTPException(status_code=409, detail='E-mail já em uso')

    if dados.nome  is not None: usuario.nome  = dados.nome
    if dados.email is not None: usuario.email = dados.email
    db.commit()
    db.refresh(usuario)
    return usuario


# DELETE /usuarios/{id} ── Soft delete
@app.delete('/usuarios/{usuario_id}')
def remover_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario or not usuario.ativo:
        raise HTTPException(status_code=404, detail='Usuário não encontrado')
    usuario.ativo = False
    db.commit()
    return {'mensagem': f'Usuário {usuario_id} removido'}