# 🛒 E-Commerce SaaS - Arquitetura Desacoplada

Este é um projeto de e-commerce simples desenvolvido como um ambiente de aprendizado focado em fundamentos profundos de engenharia de software e arquitetura desacoplada (Decoupled). O sistema conta com gerenciamento administrativo completo, controle de estoque e uma vitrine ultraveloz para o cliente final.

---

## 🏗️ Estrutura do Projeto

O repositório é dividido em duas aplicações totalmente independentes que se comunicam via requisições HTTP (APIs JSON):

```text
E-COMMERCE_THIAGO/
├── backend/           # API REST em Python & Django + Banco de Dados
└── frontend/          # Vitrine do Cliente em Astro + TypeScript
```

---

## 💻 Front-End (Vitrine do Cliente)

Desenvolvido com foco em performance absoluta, indexação de produtos no Google (SEO) e tipagem estrita de dados.

### 📦 Tecnologias e Dependências Instaladas

- **Node.js (v24+):** Ambiente de execução do JavaScript gerenciado localmente via **NVM** (Node Version Manager).
- **Astro (v6.x):** Framework moderno baseado em _Multi-Page Applications (MPA)_ e renderização no servidor (SSR) para entrega de HTML leve.
- **Vite:** Motor de compilação ultraveloz integrado nativamente ao ecossistema do Astro.
- **TypeScript (Modo Strict):** Configurado com checagem estrita de tipos para garantir a segurança dos dados do e-commerce (como contratos de produtos e carrinho).

### ⚙️ Instalação do Front-End

> Pré-requisito: ter o **NVM** instalado. Se não tiver, instale com:
>
> ```bash
> curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
> ```

```bash
# 1. Instalar e usar a versão correta do Node.js
nvm install 24
nvm use 24

# 2. Entrar na pasta do frontend
cd frontend

# 3. Criar o projeto Astro (caso esteja iniciando do zero)
npm create astro@latest

# 4. Instalar as dependências do projeto
npm install

# 5. Rodar o servidor de desenvolvimento
npm run dev
```

_Acessível localmente em: `http://localhost:4321`_

---

## 🐍 Back-End (API & Painel Administrativo)

Responsável por centralizar as regras de negócios, persistência no banco de dados, segurança de escopo por papéis (Roles) e processamento de pedidos.

### 📦 Tecnologias e Dependências Instaladas

- **Python (v3.12+):** Linguagem base executada dentro de um ambiente virtual isolado (`.venv`).
- **Django (v6.0.5):** Framework web principal utilizado como o núcleo da aplicação.
- **Django REST Framework (DRF):** Ferramenta utilizada para transformar o Django em uma fábrica de dados, servindo e recebendo dados estruturados em JSON.
- **Django Unfold:** Tema moderno baseado em Tailwind CSS utilizado para remodelar e profissionalizar o visual do **Django Admin**, gerenciando operadores e o estoque de produtos de forma visual.
- **Django CORS Headers:** Biblioteca de segurança obrigatória para gerenciar o compartilhamento de recursos de origens cruzadas, liberando o acesso seguro da API para o servidor do Astro.

### ⚙️ Instalação do Back-End

> Pré-requisito: ter o **Python 3.12+** instalado.

```bash
# 1. Entrar na pasta do backend
cd backend

# 2. Criar o ambiente virtual isolado
python -m venv .venv

# 3. Ativar o ambiente virtual
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows

# 4. Instalar todas as dependências
pip install django==6.0.5 djangorestframework==3.17.1 django-unfold==0.93.0 django-cors-headers==4.9.0

# 5. Criar o projeto Django (caso esteja iniciando do zero)
django-admin startproject setup .

# 6. Aplicar as migrações do banco de dados
python manage.py migrate

# 7. Criar um superusuário para acessar o Admin
python manage.py createsuperuser

# 8. Rodar o servidor de desenvolvimento
python manage.py runserver
```

_Acessível localmente em: `http://localhost:8000`_  
_Painel Admin em: `http://localhost:8000/admin`_

---

## 🚀 Rodando o Projeto Completo

Para rodar o projeto completo, abra dois terminais:

**Terminal 1 — Back-End:**

```bash
cd backend
source .venv/bin/activate
python manage.py runserver
```

**Terminal 2 — Front-End:**

```bash
cd frontend
npm run dev
```
