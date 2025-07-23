# SentimentAnalysis API 🤖

Análise de Sentimento como um Serviço. Uma API RESTful simples e robusta, construída com Python e FastAPI, que utiliza um modelo de Inteligência Artificial da Hugging Face para classificar o sentimento de textos em português.

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green?style=for-the-badge&logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-Ready-blue?style=for-the-badge&logo=docker)

---

## 🎯 O Problema

Empresas recebem um volume massivo de feedback em texto todos os dias — reviews de produtos, comentários em redes sociais, tickets de suporte. Analisar manualmente esse volume de dados é caro, lento e ineficiente. Esta API foi criada para resolver exatamente esse problema, fornecendo uma maneira automatizada, rápida e escalável de extrair valor desses textos.

## ✨ Features Principais

-   **Análise de Sentimento:** Classifica textos em `positive`, `negative` ou `neutral`.
-   **Score de Confiança:** Retorna a confiança do modelo na classificação, permitindo filtrar resultados de baixa precisão.
-   **API RESTful:** Fácil de integrar com qualquer aplicação, site ou outro serviço.
-   **Documentação Automática:** Interface interativa (Swagger UI) gerada automaticamente pelo FastAPI para testes e exploração da API.
-   **Pronto para Produção:** Conteinerizado com Docker e Docker Compose para portabilidade e facilidade de implantação.

## 🛠️ Stack Tecnológica

-   **Backend:** Python 3.11
-   **Framework:** FastAPI
-   **Servidor:** Uvicorn
-   **Inteligência Artificial:** Hugging Face Transformers com o modelo `cardiffnlp/twitter-xlm-roberta-base-sentiment-v2`.
-   **Conteinerização:** Docker & Docker Compose
-   **Validação de Dados:** Pydantic

## 🚀 Rodando com Docker (Método Recomendado)

Com o Docker e o Docker Compose instalados, você precisa de apenas dois comandos para ter a API funcionando.

**1. Clone o repositório:**
```bash
git clone [https://github.com/vsousadelvek/sentiment-analysis-api.git](https://github.com/vsousadelvek/sentiment-analysis-api.git)
cd sentiment-analysis-api
```

**2. Construa a imagem e inicie o contêiner:**
```bash
docker-compose up --build
```

A API estará disponível em `http://127.0.0.1:8000`.

## 📚 Uso da API

A maneira mais fácil de testar é através da documentação interativa gerada automaticamente.

-   **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Você também pode fazer uma chamada `POST` para o endpoint `/analisar` usando `curl` ou qualquer cliente de API.

**Exemplo com cURL:**
```bash
curl -X 'POST' \
  '[http://127.0.0.1:8000/analisar](http://127.0.0.1:8000/analisar)' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "texto": "Amei o produto, a entrega foi super rápida!"
}'
```

**Resposta Esperada:**
```json
{
  "sentimento": "positive",
  "confianca": 0.98
}
```

<details>
<summary><strong>Rodando Manualmente (Alternativo)</strong></summary>

Se preferir não usar o Docker, você pode rodar o projeto localmente com um ambiente virtual Python.

**1. Crie e ative um ambiente virtual:**
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

**2. Instale as dependências:**
```bash
pip install -r requirements.txt
```

**3. Inicie o servidor:**
```bash
uvicorn main:app --reload
```
</details>

---
*Criado por Delvek da Silva Venceslau de Sousa*
