# API Loja de Games

API RESTful para gerenciar o catálogo de uma loja de games: plataformas, jogos e avaliações dos clientes. Projeto final do Módulo 4 (API RESTful com FastAPI) do curso Técnico em Desenvolvimento de Sistemas, SENAI - DF.

---

## Tecnologias utilizadas

- Python 3
- FastAPI (framework da API)
- SQLAlchemy (ORM)
- SQLite (banco de dados)
- Pydantic (validação dos dados)
- Uvicorn (servidor)

## Como instalar e executar

1. Clone o repositório e entre na pasta do projeto:

```
git clone https://github.com/MMVonnSeek/dev-sistemas.git
cd modulo5-integracao
cd loja-games
```

2. Crie e ative o ambiente virtual (opcional, mas recomendado):

```
python -m venv venv
source venv/Scripts/activate        # Windows
source venv/bin/activate     # Linux/Mac
```

3. Instale as dependências:

```
pip install fastapi uvicorn sqlalchemy
```

4. Execute o servidor:

```
uvicorn main:app --reload
```

5. Acesse a documentação interativa (Swagger) em: http://127.0.0.1:8000/docs

O banco `loja_games.db` é criado automaticamente na primeira execução.

## Rotas da API

| Método | Rota                      | O que faz                          |
|--------|---------------------------|------------------------------------|
| GET    | `/plataformas/`           | Lista todas as plataformas         |
| POST   | `/plataformas/`           | Cadastra uma nova plataforma       |
| GET    | `/jogos/`                 | Lista todos os jogos               |
| GET    | `/jogos/{id}`             | Busca um jogo pelo ID              |
| POST   | `/jogos/`                 | Cadastra um novo jogo              |
| PUT    | `/jogos/{id}`             | Atualiza os dados de um jogo       |
| DELETE | `/jogos/{id}`             | Remove um jogo                     |
| GET    | `/jogos/{id}/avaliacoes`  | Lista as avaliações de um jogo     |
| POST   | `/avaliacoes/`            | Registra uma avaliação (nota 1 a 5)|
| DELETE | `/avaliacoes/{id}`        | Remove uma avaliação               |

## Autor

Max Muller — Desenvolvimento de Sistemas — SENAI-DF