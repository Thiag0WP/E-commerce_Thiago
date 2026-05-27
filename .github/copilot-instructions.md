# Instruções do Projeto — E-Commerce Thiago

Este arquivo guia o GitHub Copilot e serve como referência de boas práticas adotadas neste projeto.

---

## Arquitetura Geral

Projeto desacoplado em duas aplicações independentes que se comunicam via API REST (JSON):

- `backend/` — API em Django + PostgreSQL
- `frontend/` — Vitrine em Astro + TypeScript

---

## Back-End (Django)

### Variáveis de Ambiente

**Nunca** escrever credenciais, chaves ou configurações sensíveis diretamente no código.  
Toda configuração de ambiente usa `python-decouple` lendo de um arquivo `.env`.

```python
# CORRETO
from decouple import config
SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG", default=False, cast=bool)

# ERRADO — nunca fazer isso
SECRET_KEY = "minha-chave-secreta-aqui"
DEBUG = True
```

O arquivo `.env` **nunca vai ao git**. O `.env.example` **sempre vai ao git** como modelo.

```
backend/
  .env          ← credenciais reais (no .gitignore)
  .env.example  ← modelo sem valores reais (commitado)
```

Para criar o `.env` local:

```bash
cp backend/.env.example backend/.env
# Edite o .env com suas credenciais reais
```

### Banco de Dados

O projeto usa **PostgreSQL rodando em Docker** (não SQLite, não instalação local). A conexão é configurada via `.env`:

```
DB_NAME=nome_do_banco
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432
```

O driver utilizado é o `psycopg` (v3). O banco sobe com:

```bash
# Na raiz do projeto
docker compose up -d
```

### Docker

O `docker-compose.yml` fica na **raiz do projeto** e lê as credenciais do `backend/.env` via interpolação — nunca escrever credenciais diretamente no compose:

```yaml
# CORRETO
environment:
  POSTGRES_DB: ${DB_NAME}
  POSTGRES_USER: ${DB_USER}
  POSTGRES_PASSWORD: ${DB_PASSWORD}

# ERRADO — nunca fazer isso
environment:
  POSTGRES_DB: meu_banco
  POSTGRES_USER: admin
  POSTGRES_PASSWORD: senha123
```

### Dependências

As dependências são gerenciadas via `requirements.txt`. Após instalar qualquer novo pacote, atualizar o arquivo:

```bash
pip freeze > requirements.txt
```

Para instalar todas as dependências em um ambiente novo:

```bash
pip install -r requirements.txt
```

**Nunca** listar pacotes manualmente num `pip install` longo — sempre usar `requirements.txt`.

### Ambiente Virtual

O projeto usa `.venv` isolado dentro da pasta `backend/`. Sempre ativar antes de rodar qualquer comando:

```bash
cd backend
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows
```

---

## Front-End (Astro)

- Gerenciado com **Node.js via NVM** (não instalar Node globalmente)
- Sempre rodar `npm install` após clonar antes de `npm run dev`

---

## Fluxo para um Dev Novo no Projeto

```bash
# 1. Clonar
git clone <repo>

# 2. Subir o banco de dados
docker compose up -d

# 3. Back-end
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Editar .env com as credenciais reais
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

# 4. Front-end (outro terminal)
cd frontend
nvm use 24
npm install
npm run dev
```

---

## Regras Gerais

- Não commitar arquivos `.env`, `.venv/`, `__pycache__/`, `node_modules/` (já no `.gitignore`)
- `DEBUG=True` apenas em desenvolvimento — em produção sempre `DEBUG=False`
- `SECRET_KEY` deve ser única e gerada aleatoriamente por ambiente
- Ao adicionar uma nova variável de ambiente, atualizar também o `.env.example`
- O `docker-compose.yml` **vai ao git** — nunca colocar credenciais diretamente nele, sempre usar `${VARIAVEL}`
- Após instalar qualquer novo pacote Python, rodar `pip freeze > requirements.txt`
