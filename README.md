# Libraries

## Dependencies

- este projeto utiliza a versão 3.12 ou superior do Python.
- Poetry para gerenciar as suas dependências. 
  - Para instalar o Poetry: [guia do site oficial](https://python-poetry.org/docs/#installation)

## Criando um ambiente virtual para rodar o projeto

Usa-se o Poetry para gerenciamento de bibliotecas Python. Também é possível e recomendado a utilização do mesmo para criar o ambiente virtual do projeto. 

### Passos para criar e configurar o ambiente virtual

Utilizar o comando do poetry config para criar o ambiente virtual dentro do repositório do projeto. 

`poetry config virtualenvs.in-project = true`

Crie o ambiente virtual setando a versão 3.12 do Python (deve ter instalada na sua máquina).

`poetry env use 3.12`

Ative o ambiente virtual:

`poetry shell`

Instale as dependências do projeto:

`poetry install`

## Rodar a documentação deste projeto

execute o seguinte comando no terminal:
`make run-docs`

Abra o um navegador das internet e visualize este [link](http://127.0.0.1:8000/).
