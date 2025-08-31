# sentiment.py
from transformers import pipeline

sentiment_model = pipeline("sentiment-analysis")

def classify_comment(comment: str):
    result = sentiment_model(comment)[0]
    label = result['label']
    score = result['score']
    return label, score
