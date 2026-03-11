# nlp_service.py
from transformers import pipeline

# Тематическая классификация
classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

topic_labels = ["weather request", "country information", "travel advice", "greeting", "general question"]

def classify_message(text: str) -> str:
    result = classifier(text, topic_labels)
    return result["labels"][0]

# Тональность
sentiment_analyzer = pipeline(
    "sentiment-analysis",
    model="nlptown/bert-base-multilingual-uncased-sentiment"
)

def detect_sentiment(text: str) -> str:
    result = sentiment_analyzer(text)[0]['label']
    # Переводим звёзды в простую категорию
    if result in ["1 star", "2 stars"]:
        return "negative"
    elif result == "3 stars":
        return "neutral"
    else:
        return "positive"