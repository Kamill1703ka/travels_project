from travels_project.services.country_api import get_country_info
from travels_project.services.weather_api import get_weather
def register_handlers(bot):

    @bot.message_handler(commands=['start'])
    def start(message):
        bot.send_message(
            message.chat.id,
            "Привет! 🌍 Я Travel-бот\n\n"
            "Команды:\n"
            "/help - помощь\n"
            "/country <страна> - информация о стране\n"
            "/weather <город> - погода\n"
            "/ask <вопрос> - спросить что угодно"
        )

    @bot.message_handler(commands=['help'])
    def help_command(message):
        bot.send_message(
            message.chat.id,
            "Примеры команд:\n"
            "/country Italy\n"
            "/country Италия\n"
            "/weather Rome\n"
            "/ask Что посмотреть в Италии?"
        )

    @bot.message_handler(commands=['country'])
    def country(message):
        parts = message.text.split(" ", 1)
        if len(parts) < 2:
            bot.send_message(
                message.chat.id,
                "❌ Пожалуйста, укажи страну после команды, например: /country Italy"
            )
            return

        country_name = parts[1].strip()
        info = get_country_info(country_name)
        bot.send_message(message.chat.id, info)


    @bot.message_handler(commands=['weather'])
    def weather(message):
        parts = message.text.split(" ", 1)
        if len(parts) < 2:
            bot.send_message(
                message.chat.id,
                "❌ Пожалуйста, укажи город после команды, например: /weather Rome"
            )
            return

        city_name = parts[1].strip()
        info = get_weather(city_name)
        bot.send_message(message.chat.id, info)