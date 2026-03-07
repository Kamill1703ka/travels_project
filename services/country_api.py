# travels_project/services/country_api.py

import requests

def get_country_info(country_name):
    """
    Получает информацию о стране через API RestCountries.
    Возвращает строку с названием, столицей и населением.
    """
    try:
        url = f"https://restcountries.com/v3.1/name/{country_name}"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()[0]

        name = data["name"]["common"]
        capital = data.get("capital", ["Нет данных"])[0]
        population = data.get("population", "Нет данных")

        return f"🌍 Страна: {name}\n🏙 Столица: {capital}\n👥 Население: {population}"
    except (requests.RequestException, IndexError, KeyError):
        return "❌ Страна не найдена. Попробуйте написать точно так, как в списке стран."