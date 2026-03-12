import requests

RU_TO_EN = {
    "Италия": "Italy",
    "Франция": "France",
    "Германия": "Germany",
    "Россия": "Russia",
    "Испания": "Spain",
    "Португалия": "Portugal",
    "Швейцария": "Switzerland",
    "Китай": "China",
    "Япония": "Japan",
    "США": "United States",
    "Великобритания": "United Kingdom",
    "Канада": "Canada",
    "Мексика": "Mexico",
    "Бразилия": "Brazil",
    "Аргентина": "Argentina",
    "Чили": "Chile",
    "Перу": "Peru",
    "Колумбия": "Colombia",
    "Австралия": "Australia",
    "Новая Зеландия": "New Zealand",
    "Индия": "India",
    "Южная Корея": "South Korea",
    "Северная Корея": "North Korea",
    "Таиланд": "Thailand",
    "Вьетнам": "Vietnam",
    "Сингапур": "Singapore",
    "Малайзия": "Malaysia",
    "Индонезия": "Indonesia",
    "Филиппины": "Philippines",
    "Турция": "Turkey",
    "Греция": "Greece",
    "Австрия": "Austria",
    "Бельгия": "Belgium",
    "Нидерланды": "Netherlands",
    "Дания": "Denmark",
    "Швеция": "Sweden",
    "Норвегия": "Norway",
    "Финляндия": "Finland",
    "Польша": "Poland",
    "Чехия": "Czech Republic",
    "Словакия": "Slovakia",
    "Венгрия": "Hungary",
    "Румыния": "Romania",
    "Болгария": "Bulgaria",
    "Хорватия": "Croatia",
    "Сербия": "Serbia",
    "Словения": "Slovenia",
    "Украина": "Ukraine",
    "Беларусь": "Belarus",
    "Казахстан": "Kazakhstan",
    "Узбекистан": "Uzbekistan",
    "Грузия": "Georgia",
    "Армения": "Armenia",
    "Азербайджан": "Azerbaijan",
    "ОАЭ": "United Arab Emirates",
    "Египет": "Egypt",
    "Марокко": "Morocco",
    "ЮАР": "South Africa"
}
EN_TO_RU_COUNTRY = {
    "France": "Франция",
    "Italy": "Италия",
    "Germany": "Германия",
    "Russia": "Россия",
    "Spain": "Испания",
    "Portugal": "Португалия",
    "Switzerland": "Швейцария",
    "China": "Китай",
    "Japan": "Япония",
    "United States": "США",
    "United Kingdom": "Великобритания",
    "Canada": "Канада",
    "Brazil": "Бразилия",
    "Turkey": "Турция",
    "Greece": "Греция",
    "Australia": "Австралия"
}

EN_TO_RU_LANGUAGE = {
    "French": "Французский",
    "English": "Английский",
    "German": "Немецкий",
    "Spanish": "Испанский",
    "Italian": "Итальянский",
    "Portuguese": "Португальский",
    "Chinese": "Китайский",
    "Japanese": "Японский",
    "Russian": "Русский",
    "Arabic": "Арабский",
    "Turkish": "Турецкий",
    "Greek": "Греческий"
}
EN_TO_RU_CAPITAL = {
    "Paris": "Париж",
    "Rome": "Рим",
    "Berlin": "Берлин",
    "Madrid": "Мадрид",
    "Bern": "Берн",
    "London": "Лондон",
    "Ottawa": "Оттава",
    "Beijing": "Пекин",
    "Tokyo": "Токио",
    "Seoul": "Сеул",
    "Ankara": "Анкара",
    "Athens": "Афины",
    "Vienna": "Вена",
    "Warsaw": "Варшава",
    "Prague": "Прага",
    "Budapest": "Будапешт",
    "Bucharest": "Бухарест",
    "Belgrade": "Белград",
    "Minsk": "Минск",
    "Astana": "Астана",
    "Tashkent": "Ташкент",
    "Tbilisi": "Тбилиси",
    "Yerevan": "Ереван",
    "Baku": "Баку",
    "Abu Dhabi": "Абу-Даби"
}
def get_country_info(country):
    country_en = RU_TO_EN.get(country.title(), country)

    url = f"https://restcountries.com/v3.1/name/{country_en}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data_list = response.json()
        if not data_list:
            return f"❌ Информация о стране '{country}' не найдена."

        data = data_list[0]

        name_en = data["name"]["common"]
        name = EN_TO_RU_COUNTRY.get(name_en, name_en)

        capital_en = data.get("capital", ["Нет данных"])[0]
        capital = EN_TO_RU_CAPITAL.get(capital_en, capital_en)

        population = data.get("population", "Нет данных")

        languages_en = data.get("languages", {})
        languages = ", ".join(
            EN_TO_RU_LANGUAGE.get(lang, lang)
            for lang in languages_en.values()
        ) if languages_en else "Нет данных"

        return f"""
🌍 Страна: {name}
🏛 Столица: {capital}
👥 Население: {population}
🗣 Языки: {languages}
"""
    except requests.RequestException:
        return "❌ Ошибка при запросе к API стран (такой страны не существует)."
    except (KeyError, IndexError):
        return f"❌ Информация о стране '{country}' не найдена."