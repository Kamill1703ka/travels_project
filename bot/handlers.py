from travels_project.services.country_api import get_country_info
from travels_project.services.weather_api import get_weather
from travels_project.services.ai_generator import generate_travel_advice


def register_handlers(bot):

    @bot.message_handler(commands=['start'])
    def start(message):
        bot.send_message(
            message.chat.id,
            "Привет! 🌍 Я Travel-бот\n\n"
            "Команды:\n"
            "/help - помощь\n"
            "/country <страна>\n"
            "/weather <город>\n"
            "/ask <вопрос>\n"
            "/exit <выход>\n"
        )

    @bot.message_handler(commands=['help'])
    def help_command(message):
        bot.send_message(
            message.chat.id,
            "Примеры команд:\n"
            "/country Россия\n"
            "/weather Уфа\n"
            "/ask Что посмотреть в Уфе?"
        )

    @bot.message_handler(commands=['country'])
    def country(message):
        country_name = message.text.replace("/country", "").strip()

        if not country_name:
            bot.send_message(
                message.chat.id,
                "🌍 Введите страну.\n\nПример:\n/country Russia"
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
                "🌇 Укажите город\nПример: /weather Уфа"
            )
            return

        city_name = parts[1].strip()
        info = get_weather(city_name)

        bot.send_message(message.chat.id, info)

    @bot.message_handler(commands=['ask'])
    def ask(message):
        parts = message.text.split(" ", 1)
        if len(parts) < 2:
            bot.send_message(
                message.chat.id,
                "Напишите вопрос\n\nПример:\n/ask Что посмотреть в Японии?"
            )
            return

        question = parts[1]

        bot.send_message(message.chat.id, "🤖 Думаю...")

        answer = generate_travel_advice(question)

        bot.send_message(message.chat.id, answer)

    @bot.message_handler(commands=['exit'])
    def exit_bot(message):
        bot.send_message(
            message.chat.id,
            "👋 Спасибо за использование Travel-бота! До новых встреч."
        )