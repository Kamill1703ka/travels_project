# travels_project/services/nlp_service.py
from gliclass import GLiClassModel, ZeroShotClassificationPipeline
from transformers import AutoTokenizer

MODEL_NAME = "knowledgator/gliclass-instruct-large-v1.0"

# Загружаем модель и токенизатор
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True)
model = GLiClassModel.from_pretrained(MODEL_NAME, trust_remote_code=True)

# Создаём zero-shot pipeline
pipeline = ZeroShotClassificationPipeline(
    model=model,
    tokenizer=tokenizer,
    classification_type="multi-label",
    device=-1  # CPU; для GPU: device=0
)

# Наши классы
LABELS = [
    "Туризм",
    "Работа",
    "Учёба",
    "Общая информация",
    "Погода",
    "Еда"
]

def classify_message(text: str) -> str:
    """
    Классифицирует текст и возвращает только тему с наивысшей вероятностью.
    """
    results = pipeline(text, LABELS, threshold=0.0)[0]
    # Берем класс с наибольшей вероятностью
    best_label = max(results, key=lambda x: x["score"])["label"]
    return best_label