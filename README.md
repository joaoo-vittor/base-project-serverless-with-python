# Base project - lambda with `python`

## Preparar ambiente de desenvolvimento

- Python > 3
- Nodejs > 14

### Passo a Passo

```
python3 -m venv .venv; source .venv/bin/activate
```

```
pip install -r requirements.txt
```

```
yarn
```

### Rodar projeto

> Antes de rodar o projeto, crie um arquivo `.env` e copie o conteúdo do arquivo `.env.example` e cole dentro do arquivo `.env`.

```
yarn sls:of:dev
```

### Deploy

Para fazer o deploy configure as credenciais da `AWS`:

- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_REGION

> No arquivo `serverless.yaml` está definido a API Gateway, então pegue os ids da sua API Gateway e coloque nas envs REST_API_ID e REST_API_ROOT_RESOURCE_ID
