import requests

# Словарь русских названий в английские для RestCountries API
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
    "Великобритания": "United Kingdom"
    # добавляй остальные по мере необходимости
}

def get_country_info(country):
    country_en = RU_TO_EN.get(country, country)

    url = f"https://restcountries.com/v3.1/name/{country_en}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data_list = response.json()
        if not data_list:
            return f"❌ Информация о стране '{country}' не найдена."

        data = data_list[0]

        name = data["name"]["common"]
        capital = data.get("capital", ["Нет данных"])[0]
        population = data.get("population", "Нет данных")
        languages = ", ".join(data.get("languages", {}).values()) if data.get("languages") else "Нет данных"

        return f"""
🌍 Страна: {name}
🏛 Столица: {capital}
👥 Население: {population}
🗣 Языки: {languages}
"""
    except requests.RequestException:
        return "❌ Ошибка при запросе к API стран."
    except (KeyError, IndexError):
        return f"❌ Информация о стране '{country}' не найдена."