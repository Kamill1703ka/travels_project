from openai import OpenAI
from config import OPENROUTER_API_KEY

client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

def generate_travel_advice(question: str) -> str:
    try:
        completion = client.chat.completions.create(
            model="deepseek/deepseek-chat",
            messages=[
                {
                    "role": "system",
                    "content": "Ты туристический помощник. Отвечай на русском языке. Давай короткие списки мест,"
                               " советы путешественникам и маршруты."
                },
                {
                    "role": "user",
                    "content": question
                }
            ],
            max_tokens=1000
        )

        return completion.choices[0].message.content

    except Exception as e:
        print("AI ERROR:", e)
        return "❌ Ошибка генерации ответа."