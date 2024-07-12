<h1>Projeto Request-Data</h1> 

- Projeto que contempla o MVP para o modulo de arquitetura de software da PÓS GRADUAÇÃO de Engenharia de Software da PUC
- Esse sistema foi projeto pensando na requisição dos dados de usuário
- Foi utilizado uma API externa para requisição de dados da Receita Federal: https://cnpjs.dev/docs/api-http/
- Para simulação dos dados do cliente foi utilizado a biblioteca Faker: https://faker.readthedocs.io/en/master/


[![PyPI](https://img.shields.io/pypi/pyversions/apache-superset.svg?maxAge=2592000)](https://pypi.python.org/pypi/apache-superset)


> Status do Projeto: :heavy_check_mark: Concluido

... 

## Descrição do projeto 

<p align="justify">
  O problema que estamos abordando envolve o gerenciamento de políticas de crédito.
</p>

## Visão Geral da Solução

Na solução, foi criado um endpoint para requisição dos dados:

- customer_information


## Pré-requisitos

:warning: [Python 3.11.3](https://www.python.org/downloads/release/python-3113/)

## Funcionalidades

:heavy_check_mark: customer_information: Requisição de dados de documento PJ

No terminal, clone o projeto: 

```bash
# Clonar o projeto
git clone https://github.com/humbertoinfnet/request-data.git
```
## Utilizando VENV
Recomenda-se o uso de um ambiente virtual (virtualenv) para isolar as dependências do projeto. Para configurar e ativar um ambiente virtual, execute os seguintes comandos no terminal:
```bash
# Instalar o virtualenv, se ainda não estiver instalado
pip install virtualenv

# Criar um novo ambiente virtual
virtualenv venv

# Ativar o ambiente virtual (Windows)
venv\Scripts\activate

# Ativar o ambiente virtual (Linux/Mac)
source venv/bin/activate

# Instalação dos pacotes python
pip install -r requirements.txt
```

Rodando a aplicação com venv: 

```bash
# No diretório raiz do projeto executar o comando
python app.py
```
## Utilizando Docker
Criando imagem docker:
```bash
# No diretório raiz do projeto executar o comando
sudo docker build -t request-data .
```

Rodando a aplicação com docker: 

```bash
# No diretório raiz do projeto executar o comando
docker run -p 3001:3001 request-data
```

## Estrutura do Projeto
| Diretorio       | Diretorio              | Diretorio       | Diretorio         | Descrição                                                      |  
|---------------|----------------------|---------------|-----------------|------------------------------------------------------------------------|
| src/          |                      |               |                 | Diretório raiz do projeto                                              |
|               | entities/            |               |                 | Entidades principais do projeto, como classes ou objetos               |
|               | external_interfaces/ |               |                 | Diretório relacionado a configurações de aplicações externas           |
|               |                      | database/     |                 | Código relacionado ao banco de dados                                   |
|               |                      |               | controllers/    | Lógica de execução das consultas SQL                                   |
|               |                      |               | models/         | Definição dos modelos de tabelas                                       |
|               |                      | fastapi/      |                 | Códigos relacionado ao FastApi                                         |
|               |                      |               | routers/        | Definição das rotas da API                                             |
|               |                      |               | app             | Configurações do servidor Flask                                        |
|               |                      |               | register_route  | Código para registrar as rotas                                         |
|               | interface_adapters/  |               |                 | Códigos que fazem a interface entre casos de uso e aplicações externas |
|               | log/                 |               |                 | Configuração dos logs                                                  |
|               | use_case/            |               |                 | Casos de uso do projeto                                                |
|               |                      | request_data/ |                 | Lógica dos casos de uso relacionados ao request_data                   |
| app           |                      |               |                 | Arquivos específicos da aplicação principal                            |
| requirements  |                      |               |                 | Lista de dependências do projeto                                       |
| gitignore     |                      |               |                 | Arquivo para especificar arquivos e diretórios que devem ser ignorados pelo git |

