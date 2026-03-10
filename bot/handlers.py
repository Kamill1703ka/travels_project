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
            "/ask <вопрос>"
        )

    @bot.message_handler(commands=['help'])
    def help_command(message):
        bot.send_message(
            message.chat.id,
            "Примеры команд:\n"
            "/country Italy\n"
            "/weather Rome\n"
            "/ask Что посмотреть в Италии?"
        )

    @bot.message_handler(commands=['country'])
    def country(message):
        country_name = message.text.replace("/country", "").strip()

        if not country_name:
            bot.send_message(
                message.chat.id,
                "🌍 Введите страну.\n\nПример:\n/country Italy"
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
                "❌ Укажите город\nПример: /weather Rome"
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
                "❌ Напишите вопрос\n\nПример:\n/ask Что посмотреть в Японии?"
            )
            return

        question = parts[1]

        bot.send_message(message.chat.id, "🤖 Думаю...")

        # Используем GPT-4 через OpenAI API
        answer = generate_travel_advice(question)

        bot.send_message(message.chat.id, answer)

    @bot.message_handler(commands=['exit'])
    def exit_bot(message):
        """
        Команда выхода из бота — отправляет прощальное сообщение.
        Можно добавить очистку пользовательских данных, если они есть.
        """
        # Здесь можно очистить временные данные пользователя, если ведётся
        # user_sessions.pop(message.chat.id, None)  # пример, если есть словарь сессий

        bot.send_message(
            message.chat.id,
            "👋 Спасибо за использование Travel-бота! До новых встреч."
        )