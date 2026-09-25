# API de Cadastro de Usuários — FastAPI + Pydantic

Este projeto é uma API REST desenvolvida com **FastAPI** e **Pydantic** para demonstrar um cadastro completo de usuários.

A API implementa as principais operações de um **CRUD**:

-   **GET** → Consultar usuários
    
-   **POST** → Criar usuários
    
-   **PUT** → Atualizar usuários
    
-   **DELETE** → Excluir usuários
    

> **Observação:** neste projeto, os dados são armazenados em uma lista Python. Portanto, ela funciona como um banco de dados apenas para fins didáticos. Os dados são perdidos quando a aplicação é reiniciada.

----------

# 1. O que é FastAPI?

O **FastAPI** é um framework Python utilizado para desenvolver APIs de forma rápida, moderna e eficiente.

Ele facilita a criação de:

-   Rotas HTTP;
    
-   APIs REST;
    
-   Validação de dados;
    
-   Documentação automática;
    
-   Tratamento de erros;
    
-   Tipagem dos dados;
    
-   Integração com bancos de dados.
    

Neste projeto, o FastAPI será responsável principalmente pelas **rotas, requisições e respostas HTTP**.

----------

# 2. O que é Pydantic?

O **Pydantic** é utilizado para criar modelos e realizar a validação dos dados.

Por exemplo:

```python
class Usuario(BaseModel):
    nome: str
    email: str
    cargo: str

```

Estamos dizendo que um usuário precisa possuir:

-   `nome` → texto;
    
-   `email` → texto;
    
-   `cargo` → texto.
    

O Pydantic verifica os dados recebidos pela API antes que eles sejam processados.

----------

# 3. Estrutura geral da aplicação

O funcionamento da API pode ser representado da seguinte forma:

```text
                 CLIENTE
                    │
                    ▼
             ┌─────────────┐
             │   FastAPI   │
             └──────┬──────┘
                    │
          ┌─────────┼─────────┐
          │         │         │
         GET       POST      DELETE
          │         │         │
          ▼         ▼         ▼
       consultar  validar   procurar
          │       Pydantic     │
          │         │          │
          ▼         ▼          ▼
      usuarios_db criar      remover
          │       objeto       │
          └─────────┼──────────┘
                    │
                    ▼
                 RESPOSTA

```

----------

# 4. Importação das bibliotecas

O código começa com:

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator
from typing import Optional
from fastapi import Response

```

Vamos entender cada importação.

----------

## `FastAPI`

```python
from fastapi import FastAPI

```

`FastAPI` é a classe utilizada para criar nossa aplicação.

Quando fazemos:

```python
app = FastAPI()

```

estamos criando uma instância da aplicação.

----------

## `HTTPException`

```python
from fastapi import HTTPException

```

`HTTPException` é utilizada para informar ao cliente que ocorreu um erro HTTP.

Exemplo:

```python
raise HTTPException(
    status_code=404,
    detail="Usuário não encontrado"
)

```

A API poderá retornar:

```text
404 Not Found

```

com:

```json
{
    "detail": "Usuário não encontrado"
}

```

----------

## `BaseModel`

```python
from pydantic import BaseModel

```

`BaseModel` é a classe base utilizada para criar modelos de dados com Pydantic.

Exemplo:

```python
class Usuario(BaseModel):
    nome: str
    email: str
    cargo: str

```

----------

## `field_validator`

```python
from pydantic import field_validator

```

`field_validator` permite criar regras de validação personalizadas para determinados campos.

Neste projeto, ele será utilizado para validar o campo `nome`.

----------

## `Optional`

```python
from typing import Optional

```

`Optional` indica que determinado campo pode receber um valor ou `None`.

Exemplo:

```python
salario: Optional[float] = None

```

O salário pode ser:

```text
4500.50

```

ou:

```text
None

```

----------

## `Response`

```python
from fastapi import Response

```

`Response` permite criar uma resposta HTTP diretamente.

Será utilizado no DELETE para retornar:

```text
204 No Content

```

----------

# 5. Criando a aplicação FastAPI

```python
app = FastAPI(
    title='API de Cadastro - SENAI',
    version='0.2.0'
)

```

Aqui estamos criando nossa aplicação.

----------

## `app`

```python
app =

```

A variável `app` representa a aplicação FastAPI.

Ela será utilizada posteriormente para criar as rotas:

```python
@app.get()
@app.post()
@app.put()
@app.delete()

```

----------

## `title`

```python
title='API de Cadastro - SENAI'

```

Define o nome da aplicação.

Esse nome aparecerá na documentação automática do FastAPI.

----------

## `version`

```python
version='0.2.0'

```

Define a versão atual da API.

Exemplos:

```text
0.1.0
0.2.0
1.0.0
2.0.0

```

A utilização de versões é importante para controlar a evolução de uma API.

----------

# 6. Modelo `Usuario`

```python
class Usuario(BaseModel):

    nome: str

    email: str

    cargo: str

    ativo: bool = True

    salario: Optional[float] = None

```

Esse modelo representa os **dados recebidos pelo servidor**.

----------

#  7. Campo `nome`

```python
nome: str

```

Define que o campo `nome` deve ser um texto.

Exemplo válido:

```json
{
    "nome": "João Silva"
}

```

----------

# 8. Campo `email`

```python
email: str

```

Define que o campo `email` deve ser uma string.

Exemplo:

```json
{
    "email": "joao@email.com"
}

```

> **Importante:** `str` apenas verifica o tipo do dado. Ele não garante que o texto seja realmente um endereço de e-mail válido.

----------

# 9. Campo `cargo`

```python
cargo: str

```

Define que o cargo também deve ser um texto.

Exemplo:

```json
{
    "cargo": "Desenvolvedor"
}

```

----------

# 10. Campo `ativo`

```python
ativo: bool = True

```

O tipo:

```python
bool

```

representa valores booleanos:

```python
True
False

```

Além disso:

```python
= True

```

define um valor padrão.

Isso significa que, caso o cliente não envie `ativo`, a API utilizará:

```python
ativo = True

```

Por exemplo, o cliente pode enviar:

```json
{
    "nome": "Carlos Silva",
    "email": "carlos@email.com",
    "cargo": "Dev"
}

```

E a API considerará:

```json
{
    "nome": "Carlos Silva",
    "email": "carlos@email.com",
    "cargo": "Dev",
    "ativo": true
}

```

----------

# 11. Campo `salario`

```python
salario: Optional[float] = None

```

Vamos dividir essa declaração.

### `float`

Indica que o valor deve ser um número decimal.

Exemplos:

```text
3800.0
4500.50
3200.75

```

### `Optional`

Indica que o campo pode não possuir valor.

### `None`

Define que o valor padrão será `None`.

Portanto, podemos enviar:

```json
{
    "salario": 4500.50
}

```

ou:

```json
{
    "salario": null
}

```

Também podemos simplesmente não enviar o campo.

----------

# 12. Validação personalizada do nome

O modelo possui uma validação específica:

```python
@field_validator('nome')
@classmethod
def validar_nome(cls, v):

    v = v.strip()

    if len(v) < 3:
        raise ValueError('Nome deve ter pelo menos 3 caracteres')

    return v.title()

```

Essa função será executada quando o Pydantic validar o campo `nome`.

----------

# 13. `strip()`

```python
v = v.strip()

```

O método `strip()` remove espaços no início e no final do texto.

Por exemplo:

```text
"   joão silva   "

```

vira:

```text
"joão silva"

```

Isso ajuda a manter os dados mais organizados.

----------

# 14. `len()`

```python
if len(v) < 3:

```

`len()` retorna a quantidade de caracteres.

Exemplo:

```python
len("Max")

```

Resultado:

```text
3

```

Já:

```python
len("Jo")

```

resulta em:

```text
2

```

Portanto:

```python
if len(v) < 3:

```

significa:

> Se o nome tiver menos de 3 caracteres, o valor será considerado inválido.

----------

# 15. `raise ValueError`

```python
raise ValueError(
    'Nome deve ter pelo menos 3 caracteres'
)

```

`raise` é utilizado para lançar uma exceção.

Nesse caso, estamos informando que o valor recebido é inválido.

Se o cliente enviar:

```json
{
    "nome": "Jo",
    "email": "jo@email.com",
    "cargo": "Dev"
}

```

a validação será rejeitada.

O FastAPI normalmente retornará:

```text
422 Unprocessable Entity

```

----------

# 16. `title()`

```python
return v.title()

```

O método `title()` transforma as palavras para o formato de título.

Por exemplo:

```python
"max muller".title()

```

resulta em:

```text
"Max Muller"

```

Então:

```text
"   max muller   "

```

passará por:

```text
strip()
   ↓
"max muller"
   ↓
title()
   ↓
"Max Muller"

```

----------

# 17. Modelo `UsuarioResposta`

Agora temos:

```python
class UsuarioResposta(BaseModel):

    id: int

    nome: str

    email: str

    cargo: str

    ativo: bool

    salario: Optional[float] = None

```

Esse modelo representa os **dados devolvidos pela API**.

A principal diferença é que ele possui:

```python
id: int

```

O ID é criado pelo servidor.

----------

# 18. Por que existem dois modelos?

Temos:

```text
Usuario

```

e:

```text
UsuarioResposta

```

Eles possuem responsabilidades diferentes.

## `Usuario`

Representa os dados enviados pelo cliente.

```text
nome
email
cargo
ativo
salario

```

## `UsuarioResposta`

Representa os dados enviados pelo servidor.

```text
id
nome
email
cargo
ativo
salario

```

Isso evita que o cliente tenha que informar o ID.

Por exemplo, o cliente envia:

```json
{
    "nome": "Carlos Silva",
    "email": "carlos@email.com",
    "cargo": "Dev"
}

```

O servidor cria:

```text
id = 4

```

E responde:

```json
{
    "id": 4,
    "nome": "Carlos Silva",
    "email": "carlos@email.com",
    "cargo": "Dev",
    "ativo": true,
    "salario": null
}

```

----------

# 19. Criando o banco de dados em memória

Temos:

```python
usuarios_db: list[UsuarioResposta] = [

```

Aqui estamos criando uma lista Python.

O nome:

```python
usuarios_db

```

sugere que ela representa nosso banco de dados.

Porém, **isso não é um banco de dados real**.

É simplesmente uma lista armazenada na memória da aplicação.

----------

# 20. Usuário Alice

```python
UsuarioResposta(
    id=1,
    nome='Alice Silva',
    email='alice@email.com',
    cargo='Design',
    ativo=True,
    salario=3800.0
)

```

Cria um usuário com:

```text
ID       → 1
Nome     → Alice Silva
E-mail   → alice@email.com
Cargo    → Design
Ativo    → True
Salário  → 3800.0

```

----------

# 21. Usuário Danilo

```python
UsuarioResposta(
    id=2,
    nome='Danilo Santos',
    email='danilo@email.com',
    cargo='QA',
    ativo=True,
    salario=3200.0
)

```

Representa:

```text
ID       → 2
Nome     → Danilo Santos
E-mail   → danilo@email.com
Cargo    → QA
Ativo    → True
Salário  → 3200.0

```

----------

# 22. Usuário Max

```python
UsuarioResposta(
    id=3,
    nome='Max Muller',
    email='max@email.com',
    cargo='Dev',
    ativo=True,
    salario=4500.0
)

```

Representa:

```text
ID       → 3
Nome     → Max Muller
E-mail   → max@email.com
Cargo    → Dev
Ativo    → True
Salário  → 4500.0

```

----------

# 23. Próximo ID

```python
proximo_id = 4

```

Como já existem os IDs:

```text
1
2
3

```

o próximo usuário receberá:

```text
4

```

Depois que um novo usuário for criado:

```python
proximo_id += 1

```

o valor passará para:

```text
5

```

----------

# 24. GET `/usuarios` — Listar usuários

```python
@app.get(
    '/usuarios',
    response_model=list[UsuarioResposta]
)
def listar_usuario():

    return usuarios_db

```

Essa rota permite consultar todos os usuários.

----------

# 25. O que significa `@app.get()`?

```python
@app.get('/usuarios')

```

é um decorador de rota.

Ele informa ao FastAPI:

> Quando alguém fizer uma requisição HTTP GET para `/usuarios`, execute a função abaixo.

----------

# 26. O que é GET?

GET é utilizado principalmente para **consultar informações**.

Exemplo:

```http
GET /usuarios

```

Significa:

> Quero consultar os usuários.

----------

# 27. `response_model`

```python
response_model=list[UsuarioResposta]

```

Define o formato esperado da resposta.

A resposta será uma lista de:

```python
UsuarioResposta

```

Por exemplo:

```json
[
    {
        "id": 1,
        "nome": "Alice Silva",
        "email": "alice@email.com",
        "cargo": "Design",
        "ativo": true,
        "salario": 3800
    },
    {
        "id": 2,
        "nome": "Danilo Santos",
        "email": "danilo@email.com",
        "cargo": "QA",
        "ativo": true,
        "salario": 3200
    }
]

```

----------

# 28. Função `listar_usuario`

```python
def listar_usuario():

    return usuarios_db

```

A função simplesmente retorna a lista:

```python
usuarios_db

```

Portanto:

```http
GET /usuarios

```

retorna todos os usuários.

----------

# 29. GET `/usuarios/{usuario_id}` — Buscar por ID

```python
@app.get(
    '/usuarios/{usuario_id}',
    response_model=UsuarioResposta
)
def buscar_usuario(usuario_id: int):

```

Essa rota permite pesquisar um usuário específico.

----------

# 30. Path Parameter

Observe:

```text
/usuarios/{usuario_id}

```

O trecho:

```text
{usuario_id}

```

é um **parâmetro de caminho**, também chamado de **Path Parameter**.

Se fizermos:

```http
GET /usuarios/2

```

o FastAPI entende:

```python
usuario_id = 2

```

----------

# 31. `usuario_id: int`

```python
def buscar_usuario(usuario_id: int):

```

Indica que o ID deve ser um número inteiro.

Exemplo:

```text
/usuarios/2

```

é válido.

----------

# 32. Percorrendo os usuários

```python
for usuario in usuarios_db:

```

O `for` percorre todos os usuários.

Por exemplo:

```text
usuario = Alice
usuario = Danilo
usuario = Max

```

----------

# 33. Comparando IDs

```python
if usuario.id == usuario_id:

```

Estamos verificando se o ID do usuário atual é igual ao ID solicitado.

Se o cliente fizer:

```http
GET /usuarios/2

```

teremos:

```python
usuario_id = 2

```

Quando o loop chegar em Danilo:

```python
usuario.id == usuario_id

```

será:

```text
2 == 2

```

Resultado:

```text
True

```

----------

# 34. Retornando o usuário

```python
return usuario

```

Se o usuário for encontrado, ele será retornado.

----------

# 35. Usuário não encontrado

Se nenhum usuário possuir o ID solicitado:

```python
raise HTTPException(
    status_code=404,
    detail='Usuário não encontrado'
)

```

A API retornará:

```text
404 Not Found

```

com:

```json
{
    "detail": "Usuário não encontrado"
}

```

----------

# 36. POST `/usuarios` — Criar usuário

```python
@app.post(
    '/usuarios',
    response_model=UsuarioResposta,
    status_code=201
)
def criar_usuario(dados: Usuario):

```

Essa rota é responsável por criar um novo usuário.

----------

# 37. O que é POST?

POST é utilizado normalmente para **criar novos recursos**.

Exemplo:

```http
POST /usuarios

```

com:

```json
{
    "nome": "Carlos Silva",
    "email": "carlos@email.com",
    "cargo": "Dev",
    "ativo": true,
    "salario": 5000
}

```

----------

# 38. Status `201`

```python
status_code=201

```

O código HTTP:

```text
201 Created

```

indica que um novo recurso foi criado.

----------

# 39. Recebendo os dados

```python
def criar_usuario(dados: Usuario):

```

O parâmetro:

```python
dados: Usuario

```

informa ao FastAPI que o corpo da requisição deve seguir o modelo:

```python
Usuario

```

Por exemplo:

```json
{
    "nome": "Carlos Silva",
    "email": "carlos@email.com",
    "cargo": "Dev"
}

```

O FastAPI e o Pydantic validarão esses dados.

----------

# 40. `global proximo_id`

```python
global proximo_id

```

Essa instrução informa que queremos utilizar e modificar a variável global:

```python
proximo_id

```

Isso é necessário porque posteriormente fazemos:

```python
proximo_id += 1

```

Sem `global`, a atribuição dentro da função seria tratada como uma variável local.

----------

# 41. Verificando e-mail duplicado

```python
for u in usuarios_db:

    if u.email == dados.email:

        raise HTTPException(
            400,
            'E-mail já cadastrado'
        )

```

Antes de criar o usuário, percorremos os usuários existentes.

Para cada usuário:

```python
u

```

comparamos:

```python
u.email

```

com:

```python
dados.email

```

----------

# 42. E-mail já cadastrado

Se o e-mail já existir:

```python
raise HTTPException(
    400,
    'E-mail já cadastrado'
)

```

A API retorna:

```text
400 Bad Request

```

com:

```json
{
    "detail": "E-mail já cadastrado"
}

```

----------

# 43. Criando o novo usuário

```python
novo = UsuarioResposta(
    id=proximo_id,
    **dados.model_dump()
)

```

Essa linha merece atenção.

----------

# 44. `model_dump()`

O método:

```python
dados.model_dump()

```

converte o modelo Pydantic em um dicionário Python.

Por exemplo:

```python
{
    "nome": "Carlos Silva",
    "email": "carlos@email.com",
    "cargo": "Dev",
    "ativo": True,
    "salario": 5000
}

```

----------

# 45. O operador `**`

Temos:

```python
**dados.model_dump()

```

O `**` faz o **desempacotamento de um dicionário**.

Por exemplo:

```python
dados.model_dump()

```

pode produzir:

```python
{
    "nome": "Carlos",
    "email": "carlos@email.com",
    "cargo": "Dev"
}

```

O:

```python
**dados.model_dump()

```

permite utilizar esses valores como argumentos nomeados.

É semelhante a escrever:

```python
UsuarioResposta(
    nome="Carlos",
    email="carlos@email.com",
    cargo="Dev"
)

```

Por isso:

```python
UsuarioResposta(
    id=proximo_id,
    **dados.model_dump()
)

```

é uma forma prática de criar o objeto completo.

----------

# 46. Adicionando o usuário

```python
usuarios_db.append(novo)

```

O método:

```python
append()

```

adiciona o novo usuário ao final da lista.

Antes:

```text
Alice
Danilo
Max

```

Depois:

```text
Alice
Danilo
Max
Carlos

```

----------

# 47. Incrementando o ID

```python
proximo_id += 1

```

É equivalente a:

```python
proximo_id = proximo_id + 1

```

Se:

```text
proximo_id = 4

```

depois teremos:

```text
proximo_id = 5

```

----------

# 48. Retornando o usuário criado

```python
return novo

```

A API retorna o novo usuário.

Exemplo:

```json
{
    "id": 4,
    "nome": "Carlos Silva",
    "email": "carlos@email.com",
    "cargo": "Dev",
    "ativo": true,
    "salario": 5000
}

```

----------

# 49. PUT `/usuarios/{usuario_id}` — Atualizar

```python
@app.put(
    '/usuarios/{usuario_id}',
    response_model=UsuarioResposta
)
def atualizar_usuario(
    usuario_id: int,
    dados: Usuario
):

```

Essa rota permite atualizar um usuário.

----------

# 50. O que é PUT?

PUT é utilizado para atualizar/substituir um recurso.

Exemplo:

```http
PUT /usuarios/2

```

com:

```json
{
    "nome": "Danilo Silva",
    "email": "danilo@email.com",
    "cargo": "Dev",
    "ativo": true,
    "salario": 4000
}

```

----------

# 51. Recebendo o ID

```python
usuario_id: int

```

O ID vem da URL:

```text
/usuarios/2

```

Portanto:

```python
usuario_id = 2

```

----------

# 52. Recebendo os novos dados

```python
dados: Usuario

```

Os novos dados vêm no corpo da requisição.

Exemplo:

```json
{
    "nome": "Danilo Silva",
    "email": "danilo@email.com",
    "cargo": "Dev",
    "ativo": true,
    "salario": 4000
}

```

----------

# 53. Utilizando `enumerate()`

```python
for i, u in enumerate(usuarios_db):

```

O `enumerate()` permite obter:

-   o índice;
    
-   o elemento.
    

Por exemplo:

```text
i = 0 → Alice
i = 1 → Danilo
i = 2 → Max

```

O:

```python
i

```

representa a posição na lista.

O:

```python
u

```

representa o usuário.

----------

# 54. Encontrando o usuário

```python
if u.id == usuario_id:

```

Verificamos se o usuário atual possui o ID solicitado.

----------

# 55. Criando a versão atualizada

```python
atualizado = UsuarioResposta(
    id=usuario_id,
    **dados.model_dump()
)

```

Criamos um novo objeto `UsuarioResposta`.

O ID é mantido:

```python
id=usuario_id

```

Enquanto os outros dados vêm de:

```python
dados.model_dump()

```

----------

# 56. Substituindo o usuário

```python
usuarios_db[i] = atualizado

```

Aqui substituímos o usuário antigo pelo atualizado.

Por exemplo:

Antes:

```text
1 → Alice
2 → Danilo Santos
3 → Max

```

Depois:

```text
1 → Alice
2 → Danilo Silva
3 → Max

```

----------

# 57. Retornando o usuário atualizado

```python
return atualizado

```

A API retorna os novos dados.

----------

# 58. Usuário não encontrado no PUT

Se o ID não existir:

```python
raise HTTPException(
    404,
    'Usuário não encontrado'
)

```

A API retorna:

```text
404 Not Found

```

----------

# 59. DELETE `/usuarios/{usuario_id}`

```python
@app.delete(
    '/usuarios/{usuario_id}',
    status_code=204
)
def deletar_usuario(usuario_id: int):

```

Essa rota exclui um usuário.

----------

# 60. O que é DELETE?

DELETE é utilizado para remover um recurso.

Exemplo:

```http
DELETE /usuarios/3

```

Significa:

> Excluir o usuário que possui ID 3.

----------

# 61. Procurando o usuário

```python
for i, u in enumerate(usuarios_db):

    if u.id == usuario_id:

```

Percorremos a lista e verificamos se encontramos o ID solicitado.

----------

# 62. `pop()`

Quando encontramos:

```python
usuarios_db.pop(i)

```

O método `pop()` remove um elemento da lista utilizando seu índice.

Por exemplo:

```python
usuarios_db.pop(2)

```

remove o terceiro elemento.

----------

# 63. Status `204`

Depois da exclusão:

```python
return Response(status_code=204)

```

A API retorna:

```text
204 No Content

```

Esse código significa:

> A operação foi realizada com sucesso, mas não existe conteúdo para retornar.

----------

# 64. Usuário não encontrado no DELETE

Se o usuário não existir:

```python
raise HTTPException(
    404,
    'Usuário não encontrado'
)

```

A API retorna:

```text
404 Not Found

```

----------

# 65. CRUD completo

Nosso projeto implementa:

```text
CREATE → POST
READ   → GET
UPDATE → PUT
DELETE → DELETE

```

Podemos representar assim:

Operação

Método HTTP

Endpoint

Criar

POST

`/usuarios`

Listar

GET

`/usuarios`

Buscar

GET

`/usuarios/{id}`

Atualizar

PUT

`/usuarios/{id}`

Excluir

DELETE

`/usuarios/{id}`

----------

# 66. Exemplos de requisições

## Listar usuários

```http
GET /usuarios

```

----------

## Buscar usuário

```http
GET /usuarios/2

```

----------

## Criar usuário

```http
POST /usuarios

```

Body:

```json
{
    "nome": "Carlos Silva",
    "email": "carlos@email.com",
    "cargo": "Dev",
    "ativo": true,
    "salario": 5000
}

```

----------

## Atualizar usuário

```http
PUT /usuarios/2

```

Body:

```json
{
    "nome": "Danilo Silva",
    "email": "danilo@email.com",
    "cargo": "Desenvolvedor",
    "ativo": true,
    "salario": 4500
}

```

----------

## Excluir usuário

```http
DELETE /usuarios/2

```

----------

# 67. Principais códigos HTTP utilizados

Código

Significado

Utilização

`200`

OK

Requisição realizada com sucesso

`201`

Created

Usuário criado

`204`

No Content

Usuário excluído sem conteúdo na resposta

`400`

Bad Request

E-mail duplicado

`404`

Not Found

Usuário não encontrado

`422`

Unprocessable Entity

Dados enviados não passaram na validação

----------

# 68. Validação do Pydantic

Uma das vantagens desse projeto é que o Pydantic impede que dados incompatíveis sejam recebidos.

Por exemplo:

```python
nome: str

```

espera um texto.

E:

```python
salario: Optional[float]

```

espera um número decimal ou `None`.

Além disso, temos nossa própria regra:

```python
if len(v) < 3:

```

que impede nomes muito curtos.

----------

# 69. Responsabilidade de cada tecnologia

É importante entender que cada parte possui uma responsabilidade.

## Python

É responsável pela lógica do programa:

```text
if
for
classes
funções
listas
variáveis

```

----------

## FastAPI

É responsável principalmente por:

```text
Rotas
HTTP
Requisições
Respostas
Documentação

```

----------

## Pydantic

É responsável principalmente por:

```text
Modelos
Tipos
Validação
Tratamento dos dados

```

----------

## `usuarios_db`

É responsável pelo armazenamento temporário:

```python
list

```

Mas não é um banco de dados real.

----------

# 70. Limitação do projeto

Este projeto utiliza:

```python
usuarios_db = [...]

```

Ou seja, os dados estão armazenados na memória RAM.

Isso significa que, se a aplicação for encerrada ou reiniciada:

```text
Carlos
João
Maria

```

que foram cadastrados durante a execução serão perdidos.

Os dados iniciais voltarão a ser:

```text
Alice
Danilo
Max

```

----------

# 71. Como seria em uma aplicação real?

Em uma aplicação profissional, normalmente utilizaríamos um banco de dados.

Por exemplo:

```text
                  FastAPI
                     │
                     ▼
                Regras da API
                     │
                     ▼
                  ORM
                     │
                     ▼
              Banco de Dados
                     │
             ┌───────┴───────┐
             ▼               ▼
           MySQL         PostgreSQL

```

Poderíamos utilizar tecnologias como:

```text
FastAPI
SQLAlchemy
MySQL
PostgreSQL

```

Nesse cenário, os dados seriam persistentes.

----------

# 72. Documentação automática

Uma das grandes vantagens do FastAPI é a documentação automática.

Depois de iniciar o projeto:

```bash
uvicorn main:app --reload

```

acesse:

```text
http://127.0.0.1:8000/docs

```

O FastAPI apresentará uma interface semelhante a:

```text
GET     /usuarios
GET     /usuarios/{usuario_id}
POST    /usuarios
PUT     /usuarios/{usuario_id}
DELETE  /usuarios/{usuario_id}

```

Essa interface permite testar os endpoints diretamente pelo navegador.

----------

# 73. Executando o projeto

Supondo que o arquivo principal seja:

```text
main.py

```

podemos executar:

```bash
uvicorn main:app --reload

```

Onde:

```text
uvicorn

```

é o servidor ASGI utilizado para executar a aplicação.

```text
main

```

representa o arquivo:

```text
main.py

```

```text
app

```

representa:

```python
app = FastAPI(...)

```

E:

```text
--reload

```

faz o servidor reiniciar automaticamente quando detecta alterações no código.

----------

# 74. Estrutura simples do projeto

Uma estrutura básica pode ser:

```text
api-cadastro/
│
├── main.py
│
└── README.md

```

Onde:

```text
main.py

```

contém o código da API.

E:

```text
README.md

```

contém a documentação do projeto.

----------

# 75. Fluxo completo de criação de usuário

Imagine que o cliente envie:

```http
POST /usuarios

```

com:

```json
{
    "nome": "   joão da silva   ",
    "email": "joao@email.com",
    "cargo": "Desenvolvedor",
    "salario": 5000
}

```

A API executará aproximadamente este fluxo:

```text
1. Cliente envia requisição
          ↓
2. FastAPI recebe
          ↓
3. Pydantic valida os dados
          ↓
4. field_validator valida o nome
          ↓
5. strip() remove espaços
          ↓
6. title() ajusta o nome
          ↓
7. API verifica se o e-mail já existe
          ↓
8. API pega o próximo ID
          ↓
9. Cria UsuarioResposta
          ↓
10. Adiciona na lista
          ↓
11. Incrementa o próximo ID
          ↓
12. Retorna 201 Created

```

----------

# 76. Resumo geral

Este projeto demonstra os principais conceitos necessários para construir uma API REST simples utilizando Python.

Os principais conceitos são:

-   FastAPI;
    
-   Pydantic;
    
-   `BaseModel`;
    
-   `field_validator`;
    
-   Tipagem com Python;
    
-   `Optional`;
    
-   Rotas;
    
-   Path Parameters;
    
-   GET;
    
-   POST;
    
-   PUT;
    
-   DELETE;
    
-   Status Codes;
    
-   `HTTPException`;
    
-   `Response`;
    
-   CRUD;
    
-   Validação de dados;
    
-   `model_dump()`;
    
-   Desempacotamento com `**`;
    
-   Listas Python;
    
-   Documentação automática.
    

----------

# 77. Conceito principal

Podemos resumir toda a aplicação em quatro etapas:

```text
1. MODELO
   ↓
Pydantic define como o dado deve ser.

2. ROTA
   ↓
FastAPI define como o cliente acessa o recurso.

3. REGRA
   ↓
Python executa a lógica da operação.

4. RESPOSTA
   ↓
FastAPI/Pydantic devolvem os dados e o status HTTP.

```

E o CRUD:

```text
┌──────────┬────────────┐
│ CREATE   │ POST       │
├──────────┼────────────┤
│ READ     │ GET        │
├──────────┼────────────┤
│ UPDATE   │ PUT        │
├──────────┼────────────┤
│ DELETE   │ DELETE     │
└──────────┴────────────┘

```

----------

# Conclusão

Este projeto representa um **CRUD completo de usuários em memória**, desenvolvido com **FastAPI e Pydantic**.

Apesar de ser simples, ele apresenta conceitos fundamentais para o desenvolvimento de APIs:

```text
Cliente
   ↓
HTTP
   ↓
FastAPI
   ↓
Pydantic
   ↓
Validação
   ↓
Regra de negócio
   ↓
Dados
   ↓
Resposta HTTP

```

A partir desse projeto, é possível evoluir a aplicação para utilizar:

-   Banco de dados MySQL;
    
-   PostgreSQL;
    
-   SQLAlchemy;
    
-   Autenticação;
    
-   JWT;
    
-   Hash de senhas;
    
-   Paginação;
    
-   Filtros;
    
-   Ordenação;
    
-   Middleware;
    
-   CORS;
    
-   Testes automatizados;
    
-   Docker;
    
-   Deploy em servidor.
    

Assim, o projeto deixa de ser apenas uma API armazenada em memória e pode evoluir para uma **API completa e persistente**, semelhante às utilizadas em aplicações reais.