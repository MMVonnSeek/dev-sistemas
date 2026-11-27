# SENAI - Técnico em Desenvolvimento de Sistemas

> **Banco de Dados com Python | Gabarito - Atividade de Depuração**

----------

## Resumo dos Erros

| Erro | Arquivo | Tipo | Descrição resumida |
| ------ | -------- | ---------- | --------- |
| 1 | database.py | Sintaxe / URL | URL do SQLite com apenas duas barras (`sqlite://`) em vez de três (`sqlite:///`) |
| 2 | database.py | Lógica SQLAlchemy | `autocommit=True` e `autoflush=True` — ambos devem ser `False` |
|3 | models.py | Nome de tabela | `__tablename__ = "fornecedor"` conflita com `ForeignKey("fornecedores.id")` |
| 4 | models.py | Tipo de coluna | `preco` definido como `String(20)` em vez de `Float` |
| 5 | models.py | Tipo de coluna | `quantidade` definida como `Boolean` em vez de `Integer` |
| 6 | main.py | Ordem de operações | `forn2` e `forn3` nunca receberam `db.add()` antes do `commit()` |
| 7 | main.py | Lógica SQLAlchemy | `db.refresh()` chamado sem `db.commit()` anterior para os produtos |
| 8 | main.py | AttributeError | `prod.unidade` não existe no model `Produto` |
| 9 | crud.py | Classe inexistente | A classe `Banco_de_dados` não existe |

----------

## Erro 1 — URL do banco de dados mal formada (database.py)

**Linha(s) com erro:**
```
DATABASE_URL = "sqlite://estoque_construcao.db"
```

**Linha(s) corrigida(s):**
```
DATABASE_URL = "sqlite:///./estoque_construcao.db"
```

**Explicação:**

A URL do SQLite exige três barras após o protocolo (`sqlite:///`). Com apenas duas barras, o SQLAlchemy interpreta a string como uma URL de rede relativa inválida e lança um erro ao tentar criar o engine. As três barras indicam um caminho de arquivo local — a terceira inicia o caminho relativo ao diretório atual.

----------

## Erro 2 — autocommit e autoflush incorretos (database.py)

**Linha(s) com erro:**
```
SessionLocal = sessionmaker(autocommit=True, autoflush=True, bind=engine)
```

**Linha(s) corrigida(s):**
```
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
```

**Explicação:**

Com `autocommit=True`, cada operação é confirmada individualmente no banco, impedindo o uso de transações. Se uma inserção falhar, as anteriores já terão sido salvas sem possibilidade de rollback. Com `autoflush=True`, o SQLAlchemy sincroniza automaticamente antes de cada consulta, podendo causar erros ao lidar com objetos ainda incompletos. O padrão recomendado é manter ambos como `False`.

----------

## Erro 3 — `__tablename__` diverge do ForeignKey (models.py)

**Linha(s) com erro:**
```
__tablename__ = "fornecedor"
```

**Linha(s) corrigida(s):**
```
__tablename__ = "fornecedores"
```

**Explicação:**

O model `Produto` declara `ForeignKey("fornecedores.id")`, referenciando uma tabela chamada `"fornecedores"`. Porém, o model `Fornecedor` cria a tabela com o nome `"fornecedor"` (singular). Essa divergência faz o SQLAlchemy lançar um erro ao criar as tabelas, pois a chave estrangeira aponta para um nome de tabela inexistente.

----------

## Erro 4 — tipo errado para `preco`: String em vez de Float (models.py)

**Linha(s) com erro:**
```
preco = Column(String(20), nullable=False)
```

**Linha(s) corrigida(s):**
```
preco = Column(Float, nullable=False)
```

**Explicação:**

O campo `preco` armazena valores monetários, que são números de ponto flutuante. Definido como `String(20)`, o banco aceita qualquer texto no campo — inclusive valores inválidos. Além disso, operações matemáticas (soma, média, comparação) sobre esse campo produziriam resultados incorretos ou erros, pois o Python trataria os valores como strings.

----------

## Erro 5 — tipo errado para `quantidade`: Boolean em vez de Integer (models.py)

**Linha(s) com erro:**
```
quantidade = Column(Boolean, default=0)
```

**Linha(s) corrigida(s):**
```
quantidade = Column(Integer, default=0)
```

**Explicação:**

`Boolean` armazena apenas dois valores: `True` (1) ou `False` (0). Qualquer quantidade maior que 1 será convertida para `True` (equivalente a 1), tornando impossível controlar o estoque real. O tipo correto é `Integer`, que suporta qualquer número inteiro positivo ou negativo.

----------

## Erro 6 — `forn2` e `forn3` nunca adicionados à sessão (main.py)

**Linha(s) com erro:**
```
db.add(forn1)
db.commit()
db.refresh(forn2)  # forn2 nunca teve db.add()
```

**Linha(s) corrigida(s):**
```
db.add(forn1)
db.add(forn2)
db.add(forn3)
db.commit()
db.refresh(forn1)
db.refresh(forn2)
db.refresh(forn3)
```

**Explicação:**

Apenas `forn1` recebeu `db.add()` antes do `commit()`. Os objetos `forn2` e `forn3` foram criados em memória, mas nunca foram adicionados à sessão do SQLAlchemy. Ao chamar `db.refresh()` nesses objetos, o SQLAlchemy tentará recarregar do banco um registro que nunca foi salvo, lançando um erro de instância desanexada (`DetachedInstanceError`) ou similar.

----------

## Erro 7 — `db.refresh()` chamado sem `db.commit()` para os produtos (main.py)

**Linha(s) com erro:**
```
for p in produtos:
 db.refresh(p)  # commit() nunca foi chamado
```

**Linha(s) corrigida(s):**
```
db.commit()
for p in produtos:
 db.refresh(p)
```

**Explicação:**

O método `db.refresh()` recarrega o estado de um objeto a partir do banco. Para isso funcionar, o objeto precisa ter sido persistido antes com `db.commit()`. Sem o commit, os produtos ainda estão apenas na memória da sessão e não possuem IDs gerados pelo banco. A chamada a `refresh()` falhará ou retornará dados inconsistentes.

----------

## Erro 8 — atributo inexistente: `prod.unidade` (main.py)

**Linha(s) com erro:**
```
print(f" [{prod.id}] {prod.nome} | R$ {prod.preco:.2f} | Un.: {prod.unidade}")
```

**Linha(s) corrigida(s):**
```
print(f" [{prod.id}] {prod.nome} | R$ {prod.preco:.2f} | Qtd: {prod.quantidade}")
```

**Explicação:**

O model `Produto` não possui o atributo `unidade`. Ao tentar acessar `prod.unidade`, o Python lança `AttributeError: 'Produto' object has no attribute 'unidade'`. O atributo correto para exibir a quantidade disponível em estoque é `prod.quantidade`, que está devidamente definido no model.

----------

## Erro 9 — Classe inexistente (crud.py)

**Linha(s) com erro:**
```
from app.models import Categoria, Fornecedor, Produto, Banco_de_dados
```

**Linha(s) corrigida(s):**
```
from app.models import Categoria, Fornecedor, Produto
```

**Explicação:**

A classe `Banco_de_dados` não existe no arquivo `models.py`. Ao importar e tentar acessar a classe, ela aparece como inexistente. Basta apagá-la, pois usaremos apenas as classes declaradas no arquivo `models.py`: `Categoria`, `Fornecedor` e `Produto`.