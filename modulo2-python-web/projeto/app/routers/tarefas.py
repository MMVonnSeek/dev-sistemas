from fastapi import APIRouter, HTTPException, Path, Query, Response
from typing import Annotated, Optional
from app.models import TarefaEntrada, TarefaSaida, TarefaParcial
from app.models import StatusEnum, PrioridadeEnum

router = APIRouter(prefix='/tarefas', tags=['Tarefas'])

# Banco simulado
banco: list[TarefaSaida] = [
    TarefaSaida(id=1, titulo='Configurar ambiente Python', responsavel='Carlos', prioridade='alta', status='concluida'),
    TarefaSaida(id=2, titulo='Criar modelos Pydantic', responsavel='Ana',    prioridade='alta', status='concluida'),
    TarefaSaida(id=3, titulo='Implementar CRUD completo', responsavel='Carlos', prioridade='critica', status='em_andamento'),
    TarefaSaida(id=4, titulo='Conectar ao banco MySQL', responsavel='Bruno',  prioridade='alta', status='pendente'),
    TarefaSaida(id=5, titulo='Escrever documentacao', responsavel='Ana',    prioridade='baixa', status='pendente'),
]
proximo_id = 6

# GET /tarefas/estatisticas -- ANTES de /{tarefa_id}
@router.get('/estatisticas', summary='Estatisticas gerais das tarefas')
def estatisticas():
    por_status = {s.value: sum(1 for t in banco if t.status == s) for s in StatusEnum}
    por_prioridade = {p.value: sum(1 for t in banco if t.prioridade == p) for p in PrioridadeEnum}
    return {
        'total': len(banco),
        'por_status': por_status,
        'por_prioridade':por_prioridade,
    }

# GET /tarefas
@router.get('/', response_model=list[TarefaSaida], summary='Lista tarefas com filtros')
def listar(
    status: Annotated[Optional[StatusEnum], Query(description='Filtrar por status')] = None,
    prioridade: Annotated[Optional[PrioridadeEnum], Query(description='Filtrar por prioridade')] = None,
    responsavel: Annotated[Optional[str], Query(description='Filtrar por responsavel')] = None,
    limite: Annotated[int, Query(ge=1, le=100)] = 20,
    pagina: Annotated[int, Query(ge=1)] = 1,
):
    resultado = banco
    if status: resultado = [t for t in resultado if t.status == status]
    if prioridade: resultado = [t for t in resultado if t.prioridade == prioridade]
    if responsavel: resultado = [t for t in resultado if responsavel.lower() in (t.responsavel or '').lower()]
    inicio = (pagina - 1) * limite
    return resultado[inicio : inicio + limite]

# GET /tarefas/{tarefa_id}
@router.get('/{tarefa_id}', response_model=TarefaSaida, summary='Busca uma tarefa pelo ID')
def buscar(tarefa_id: Annotated[int, Path(ge=1)]):
    for t in banco:
        if t.id == tarefa_id: return t
    raise HTTPException(status_code=404, detail='Tarefa nao encontrada')

# POST /tarefas
@router.post('/', response_model=TarefaSaida, status_code=201, summary='Cria uma nova tarefa')
def criar(dados: TarefaEntrada):
    """
    Cria uma nova tarefa no sistema.
    - **titulo**: obrigatorio, 3 a 120 caracteres
    - **prioridade**: padrao 'media' se nao informada
    - **status**: padrao 'pendente' para novas tarefas
    - **prazo**: formato ISO 8601 -- YYYY-MM-DD
    """
    global proximo_id
    nova = TarefaSaida(id=proximo_id, **dados.model_dump())
    banco.append(nova)
    proximo_id += 1
    return nova

# PUT /tarefas/{tarefa_id}
@router.put('/{tarefa_id}', response_model=TarefaSaida, summary='Substitui uma tarefa inteira')
def atualizar(tarefa_id: Annotated[int, Path(ge=1)], dados: TarefaEntrada):
    for i, t in enumerate(banco):
        if t.id == tarefa_id:
            banco[i] = TarefaSaida(id=tarefa_id, **dados.model_dump())
            return banco[i]
    raise HTTPException(status_code=404, detail='Tarefa nao encontrada')

# PATCH /tarefas/{tarefa_id}
@router.patch('/{tarefa_id}', response_model=TarefaSaida, summary='Atualiza campos especificos')
def atualizar_parcial(tarefa_id: Annotated[int, Path(ge=1)], dados: TarefaParcial):
    for i, t in enumerate(banco):
        if t.id == tarefa_id:
            atual = t.model_dump()
            atual.update(dados.model_dump(exclude_none=True))
            banco[i] = TarefaSaida(**atual)
            return banco[i]
    raise HTTPException(status_code=404, detail='Tarefa nao encontrada')

# DELETE /tarefas/{tarefa_id}
@router.delete('/{tarefa_id}', status_code=204, summary='Remove uma tarefa')
def deletar(tarefa_id: Annotated[int, Path(ge=1)]):
    for i, t in enumerate(banco):
        if t.id == tarefa_id:
            banco.pop(i)
            return Response(status_code=204)
    raise HTTPException(status_code=404, detail='Tarefa nao encontrada')
