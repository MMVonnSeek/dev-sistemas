from fastapi import APIRouter, HTTPException, Path, Query, Response
from typing import Annotated, Optional
from app.models import UsuarioEntrada, UsuarioSaida, UsuarioParcial

# O router substitui o 'app' para as rotas deste arquivo
# prefix='/usuarios': todas as rotas começam com /usuarios
# tags=['Usuários']: agrupa as rotas no Swagger
router = APIRouter(prefix='/usuarios', tags=['Usuários'])

# Banco Simulado - mesmo que tinhamos no main.py
banco: list[UsuarioSaida] = [
    UsuarioSaida(id=1, nome='Fulano', email='fulano@email.com', 
                 cargo='Dev', ativo=True, salario=4500.0),
    UsuarioSaida(id=2, nome='Beltrano', email='beltrano@email.com', 
                 cargo='Designer', ativo=True, salario=3500.0),
    UsuarioSaida(id=3, nome='Sicrano', email='sicrano@email.com', 
                 cargo='QA', ativo=False, salario=3200.0),
]
proximo_id = 4

# GET /usuarios - lista com filtros e páginação
@router.get('/', response_model=list[UsuarioSaida], summary='Lista usuários')
def listar_usuarios(
    ativo: Annotated[Optional[bool], Query(description='Filtrar por status')] = None,
    cargo: Annotated[Optional[str], Query(description='Filtrar por cargo')] = None,
    limite: Annotated[int, Query(ge=1, le=100, description='Itens por página')] = 10,
    pagina: Annotated[int, Query(ge=1, description='Número da página')] = 1,
):
    resultado = banco
    if ativo is not None:
        resultado = [user for user in resultado if user.ativo==ativo]
    if cargo:
        resultado = [user for user in resultado if user.cargo.lower() == cargo.lower()]
    inicio = (pagina - 1) * limite
    return resultado[inicio : inicio + limite]

# GET /usuarios/{usuario_id} - busca por id
@router.get('/usuario_id', response_model=UsuarioSaida)
def buscar_usuario(
    usuario_id: Annotated[int, Path(ge=1, description='ID do usuário')]
):
    for user in banco:
        if user.id == usuario_id:
            return user
        raise HTTPException(status_code=404, detail='Não encontrado')

# POST /usuarios - criar
@router.post('/', response_model=UsuarioSaida, status_code=201)
def criar_usuario(dados: UsuarioEntrada):
    global proximo_id
    for user in banco:
        if user.email == dados.email:
            raise HTTPException(400, 'E-mail já cadastrado')
    novo = UsuarioSaida(id=proximo_id, **dados.model_dump())
    banco.append(novo)
    proximo_id += 1
    return novo

# PUT /usuarios/{usuario_id} - substitui tudo
@router.put('/{usuario_id}', response_model=UsuarioSaida)
def atulizar_usuario(
    usuario_id: Annotated[int, Path(ge=1)],
    dados: UsuarioEntrada
):
    for valor, user in enumerate(banco):
        if user.id == usuario_id:
            banco[valor] = UsuarioSaida(id=usuario_id, **dados.model_dump())
        return banco[valor]
    raise HTTPException(404, 'Não Encontrado')

# PATH /usuarios/{usuario_id} - Atualiza campos específicos
@router.patch('/{usuario_id}', response_model=UsuarioSaida)
def atualizar_parcial(
    usuario_id: Annotated[int, Path(ge=1)],
    dados: UsuarioParcial
):
    for valor, user in enumerate(banco):
        if user.id == usuario_id:
            atual =user.model_dump()
            atual.update(dados.model_dump(exclude_none=True))
            banco[valor] = UsuarioSaida(**atual)
            return banco[valor]
        raise HTTPException(404, 'Não encontrado')

# DELETE /usuarios/{usuario_id} - remover
@router.delete('/{usuario_id}', status_code=204)
def deletar_usuario(
    usuario_id: Annotated[int, Path(ge=1)]
):
    for valor, user in enumerate(banco):
        if user.id == usuario_id:
            banco.pop(valor)
            return Response(status_code=204)
        raise HTTPException(404, 'Não encontrado')
