
#autor: Delvek (chuchu)


from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
import logging

# Configuração básica de logging para ver informações no console
logging.basicConfig(level=logging.INFO)

# --- Carregamento do Modelo de IA ---
# O modelo será baixado da Hugging Face na primeira vez que o código rodar.
# Isso pode levar alguns minutos e requer conexão com a internet.
try:
    logging.info("Carregando o modelo de análise de sentimento...")

    # CORREÇÃO AQUI: Trocamos para um modelo multilíngue que funciona bem com português.
    sentiment_pipeline = pipeline(
        "sentiment-analysis",
        model="nlptown/bert-base-multilingual-uncased-sentiment"
    )

    logging.info("Modelo carregado com sucesso!")
except Exception as e:
    logging.error(f"Erro ao carregar o modelo: {e}")
    sentiment_pipeline = None

# --- Definição da Aplicação FastAPI ---
app = FastAPI(
    title="SentimentAnalysis API",
    description="Uma API simples para analisar o sentimento de textos em português.",
    version="1.0.0"
)


# --- Modelos de Dados (Request e Response) ---
class SentimentRequest(BaseModel):
    texto: str


class SentimentResponse(BaseModel):
    sentimento: str
    confianca: float


# --- Endpoint da API ---
@app.post("/analisar", response_model=SentimentResponse)
def analisar_sentimento(request: SentimentRequest):
    """
    Recebe um texto e retorna o sentimento analisado (positive, negative ou neutral)
    e um score de confiança.
    """
    if not sentiment_pipeline:
        return {
            "sentimento": "erro",
            "confianca": 0.0
        }

    # Renomeamos as labels do modelo para o nosso padrão.
    # O modelo original retorna 'positive', 'negative', 'neutral'.
    # A lógica abaixo continua válida.
    resultado = sentiment_pipeline(request.texto)

    sentimento_analisado = resultado[0]['label']
    confianca = resultado[0]['score']

    return SentimentResponse(sentimento=sentimento_analisado, confianca=confianca)


# --- Endpoint Raiz ---
@app.get("/")
def root():
    return {"message": "SentimentAnalysis API está no ar!"}