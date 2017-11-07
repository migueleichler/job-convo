# Teste de Código Python/Django

## Instruções:

- Primeiro, escolha um repositório para trabalhar e clone este repositório:

```
git clone git@github.com:migueleichler/job-convo.git
```

Ou:

```
git clone https://github.com/migueleichler/job-convo.git
```

- Acesse o diretório do Projeto:

```
cd job-convo
```

- Dentro do diretório crie um Virtual Enviroment:

```
python -m venv .venv

source .venv/bin/activate
```

- Com a Virtual Enviroment ativada instale as dependências do projeto:

```
pip install -r requirements.txt
```

- Em seguida, realizar a migração do banco de dados:

```
manage.py migrate
```

- Após a migração utilizar o comando abaixo para importar os grupos de Usuário (Candidato e Empresa) e suas respectivas permissões:

```
manage.py loaddata core/fixtures/fixtures.json
```
