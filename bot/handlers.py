from travels_project.services.country_api import get_country_info
from travels_project.services.weather_api import get_weather
from travels_project.services.ai_generator import generate_travel_advice
from travels_project.services.nlp_service import classify_message, detect_sentiment


def register_handlers(bot):

    @bot.message_handler(commands=['start'])
    def start(message):

        bot.send_message(
            message.chat.id,
            "Привет! 🌍 Я Travel-бот\n\n"
            "Я умею:\n"
            "🌤 показывать погоду\n"
            "🌍 рассказывать о странах\n"
            "✈ давать советы путешественникам\n\n"
            "Команды:\n"
            "/country Italy\n"
            "/weather Rome\n"
            "/ask Что посмотреть в Италии?"
        )


    @bot.message_handler(commands=['help'])
    def help_command(message):

        bot.send_message(
            message.chat.id,
            "Примеры:\n\n"
            "/country Italy\n"
            "/weather Rome\n"
            "/ask Что посмотреть в Японии?"
        )


    @bot.message_handler(commands=['country'])
    def country(message):

        country_name = message.text.replace("/country", "").strip()

        if not country_name:
            bot.send_message(
                message.chat.id,
                "Введите страну.\n\nПример:\n/country Italy"
            )
            return

        info = get_country_info(country_name)

        bot.send_message(message.chat.id, info)

    @bot.message_handler(commands=['weather'])
    def weather(message):

        parts = message.text.split(" ", 1)

        if len(parts) < 2:
            bot.send_message(
                message.chat.id,
                "Укажите город\n\nПример:\n/weather Rome"
            )
            return

        city = parts[1]

        info = get_weather(city)

        bot.send_message(message.chat.id, info)


    # ---------- ASK (AI) ----------

    @bot.message_handler(commands=['ask'])
    def ask(message):

        parts = message.text.split(" ", 1)

        if len(parts) < 2:
            bot.send_message(
                message.chat.id,
                "Напишите вопрос\n\nПример:\n/ask Что посмотреть в Италии?"
            )
            return

        question = parts[1]

        bot.send_message(message.chat.id, "🤖 Думаю...")

        answer = generate_travel_advice(question)

        bot.send_message(message.chat.id, answer)


    # ---------- УМНОЕ СООБЩЕНИЕ (NLP) ----------

    @bot.message_handler(func=lambda message: True)
    def smart_reply(message):

        text = message.text

        topic = classify_message(text)

        sentiment = detect_sentiment(text)

        print("Тема:", topic)
        print("Тональность:", sentiment)


        if topic == "weather request":

            bot.send_message(
                message.chat.id,
                "Похоже вы спрашиваете про погоду.\n\nПопробуйте:\n/weather Rome"
            )


        elif topic == "country information":

            bot.send_message(
                message.chat.id,
                "Похоже вы спрашиваете о стране.\n\nПопробуйте:\n/country Italy"
            )


        elif topic == "travel advice":

            bot.send_message(message.chat.id, "✈ Сейчас подумаю...")

            answer = generate_travel_advice(text)

            bot.send_message(message.chat.id, answer)


        elif topic == "greeting":

            bot.send_message(
                message.chat.id,
                "Привет! 👋\n\nЯ Travel-бот.\nСпроси меня о путешествиях!"
            )


        else:

            bot.send_message(
                message.chat.id,
                "Я не совсем понял запрос.\n\nПопробуйте:\n"
                "/weather Rome\n"
                "/country Italy\n"
                "/ask Что посмотреть в Японии?"
            )