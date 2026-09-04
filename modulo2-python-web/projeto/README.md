# ATIVIDADE - Expandindo a API de Tarefas

> **SENAI** | Desenvolvimento de Sistemas - Módulo 2 | Python para Web

[![Curso](https://img.shields.io/badge/Curso-Desenvolvimento_de_Sistemas-009688?style=for-the-badge)](https://github.com/mmvonnseek/uc-desenvolvimento-apis)
[![Instituição](https://img.shields.io/badge/Instituição-SENAI-orange?style=for-the-badge)](https://github.com/mmvonnseek/uc-desenvolvimento-apis)
[![Professor](https://img.shields.io/badge/Professor-Max_Muller-black?style=for-the-badge)](https://github.com/MMVonnSeek)
[![Python](https://img.shields.io/badge/Python-3.10+-00bfe3?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
----------

### Clone o repositório

```
git clone https://github.com/MMVonnSeek/dev-sistemas.git
cd modulo2-python-web
cd projeto
```


## O que você deve implementar

Trabalhando nos arquivos da pasta `projeto`, adicione as seguintes funcionalidades à API de Tarefas.

----------

## Parte 1 - Novas rotas na API

**Arquivo:** `app/routers/tarefas.py`

### a) GET /tarefas/responsavel/{nome}

Retorna todas as tarefas de um responsável específico.

**Requisitos:**

-   Usar `Path` com `min_length=2`
-   Retornar `404` se nenhuma tarefa for encontrada para aquele responsável

----------

### b) PATCH /tarefas/{tarefa_id}/status

Rota dedicada apenas para mudar o status da tarefa.

**Requisitos:**

-   Receber um body simples com apenas o campo `status` (`StatusEnum`)
-   Retornar `400` se tentar mudar uma tarefa **cancelada** para qualquer outro status

----------

### c) GET /tarefas/prioridade/critica

Retorna apenas as tarefas com prioridade **crítica** e status **diferente** de `concluída` ou `cancelada`.

**⚠️ Importante:** Esta rota deve aparecer **ANTES** de `/{tarefa_id}` no arquivo.

----------

## Parte 2 - Melhorias nos modelos

**Arquivo:** `app/models.py`

### a) Campo `criado_em`

Adicionar o campo `criado_em` do tipo `date` em `TarefaSaida`, com a data atual como padrão.

**Dica:** Use `date.today()`

----------

### b) Campo `tags`

Adicionar o campo `tags` do tipo `list[str]` em:

-   `TarefaEntrada` (padrão: lista vazia)
-   `TarefaSaida` (padrão: lista vazia)

**Validador:** Converter cada tag para **minúsculo** e remover **duplicatas**.

----------

## Parte 3 - Atualizar o front-end

**Arquivo:** `front/app.js`

### a) Busca por responsável

Adicionar um campo de busca por responsável no painel de filtros.

**Requisitos:**

-   Ao clicar em **Filtrar**, incluir o `responsavel` como query parameter se o campo estiver preenchido

### b) Exibir tags nos cards

Exibir as **tags** de cada tarefa no card como **badges azuis**, se existirem.

----------

## Desafio Extra (Não obrigatório)

### Sistema de Comentários

Criar um modelo `Comentario` com os campos:

-   `id`
-   `tarefa_id`
-   `autor` (str)
-   `texto` (str)

**Rotas a adicionar:**

Método

Endpoint

Descrição

`POST`

`/tarefas/{tarefa_id}/comentarios`

Adicionar comentário

`GET`

`/tarefas/{tarefa_id}/comentarios`

Listar comentários

**Requisitos:**

-   Retornar `404` se a tarefa não existir
-   Manter os comentários em uma lista separada no router
-   Filtrar por `tarefa_id` na listagem

----------

## Requisitos Técnicos

Requisito

Descrição

**Ordem das rotas**

`/tarefas/prioridade/critica` e `/tarefas/responsavel/{nome}` DEVEM vir **antes** de `/tarefas/{tarefa_id}`

**Validador de tags**

Usar `set()` para remover duplicatas e retornar `list`

**Status cancelado**

`PATCH /tarefas/{tarefa_id}/status` deve retornar `400` se tentar mudar tarefa cancelada

**Testes**

Testar todas as novas rotas no Swagger antes de atualizar o front-end

----------

## Como Entregar

Envie o **link do repositório** pelo **Google Classroom**.


<div align="center">

**Bom trabalho! 🚀**


---

## Autor

**Max Muller**
Professor · SENAI-DF

[![GitHub](https://img.shields.io/badge/GitHub-MMVonnSeek-181717?style=flat&logo=github)](https://github.com/MMVonnSeek)

</div>
