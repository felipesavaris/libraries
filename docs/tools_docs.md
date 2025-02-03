# REferências de estudo

## alembic

- doc oficial: https://alembic.sqlalchemy.org/en/latest/front.html#dependencies
- live de python: https://www.youtube.com/watch?v=yQtqkq9UkDA

iniciar migrações com o alembic: 
`alembic init <qualquer-nome>`

aplicar migração:
- primeiro é necessário configurar:
  - mover o arquivo alembic.ini para dentro da pasta <qualquer-nome>
  - alembic.ini -> script_location (caminho de onde vai criar/rodar)
  - alembic.ini -> sqlalchemy (dados do banco de dados. Iniciarei com o sqlite)
    - sqlalchemy.url = sqllite:///libraries.db

`alembic -c src/adapters/outbound/db/alembic/alembic.ini revision --autogenerate -m "create_users_table"``

`alembic upgrade head`

caso precise reverter uma migração:
`alembic downgrade -1`

## Problemas conhecidos:

- Migração gerada vazia, sem alteração na tipagem coluna

Para fazer com que o Alembic seja sensível a alteracão de tipos é preciso configurar no arquivo `env.py` e adicionar no contexto das funções de migrações online e offline o seguinte parâmetro: `compare_type=True,`.

- Erro ao gerar migration referente a `near "ALTER": syntax error`

Erro comum no SQLITE ou até mesmo quando ocorre um problema de instabilidade no banco de dados, o erro ocorre por não conseguir fazer mais de uma alteração por vez, exemplo: alterar uma coluna e popular a mesma. 
Faz-se necessária a configuração em batch. Exemplo:

```python 
def upgrade() -> None:
    with op.batch_alter_table('column_name', schema=None) as batch_op:
        batch_op.alter_column('name', ...)
```

Também será necessário aplicar o uso de *batch* na função de **downgrade**. 

ALTERNATIVA:
Em vez de usar o modo acima em *batch*, é possível configurar o *context* do arquivo `env.py` para receber o parâmetro `render_as_batch=True`.
