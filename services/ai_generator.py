# travels_project/services/ai_generator.py

from openai import OpenAI
from config import OPENAI_API_KEY  # импорт ключа

# Инициализация клиента OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)

def generate_travel_advice(question: str) -> str:
    """
    Генерирует ответ про путешествия на русском с помощью Qwen 3.5
    """
    prompt = f"Ты — эксперт по путешествиям. Дай полный ответ на русском:\n{question}"

    response = client.chat.completions.create(
        model="qwen-3.5",  # заменили модель
        messages=[
            {"role": "system", "content": "Ты эксперт по путешествиям."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300,
        temperature=0.7
    )

    # В Qwen 3.5 структура ответа аналогична
    return response.choices[0].message["content"].strip()


# Тест
if __name__ == "__main__":
    print(generate_travel_advice("Что посмотреть в России за 7 дней?"))