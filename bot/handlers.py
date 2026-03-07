from services.country_api import get_country_info

def register_handlers(bot):

    @bot.message_handler(commands=['start'])
    def start(message):
        bot.send_message(message.chat.id,
        "Привет! 🌍 Я Travel-бот\n\n"
        "Команды:\n"
        "/help\n"
        "/country\n"
        "/weather\n"
        "/ask")

    @bot.message_handler(commands=['help'])
    def help_command(message):
        bot.send_message(message.chat.id,
        "Команды:\n"
        "/country Italy\n"
        "/weather Rome\n"
        "/ask Что посмотреть в Италии?")

    @bot.message_handler(commands=['country'])
    def country(message):

        country = message.text.split(" ")[1]

        info = get_country_info(country)

        bot.send_message(message.chat.id, info)