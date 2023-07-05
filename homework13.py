import requests
from datetime import datetime

class CurrencyConverter:
    def __init__(self):
        self.base_url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"

    def get_exchange_rate(self, date=None):
        if date:
            try:
                date_obj = datetime.strptime(date, "%Y-%m-%d")
                formatted_date = date_obj.strftime("%Y%m%d")
                url = f"{self.base_url}&date={formatted_date}"
            except ValueError:
                print("Невірний формат дати. Використайте формат 'YYYY-MM-DD'.")
                return None
        else:
            url = self.base_url

        response = requests.get(url)
        data = response.json()

        return data

    def save_exchange_rate_to_file(self, data, file_path):
        current_date = datetime.now().strftime("%Y-%m-%d")

        with open(file_path, "w") as file:
            file.write(f"[дата, на яку актуальний курс: {current_date}]\n")

            for index, currency in enumerate(data, start=1):
                currency_name = currency.get("txt", "Невідома валюта")
                exchange_rate = currency.get("rate", "Невідомий курс")
                file.write(f"{index}. {currency_name} to UAH: {exchange_rate}\n")


converter = CurrencyConverter()
date_input = input("Введіть дату у форматі 'YYYY-MM-DD' (або натисніть Enter для отримання поточного курсу): ")

if date_input:
    try:
        datetime.strptime(date_input, "%Y-%m-%d")
    except ValueError:
        print("Невірний формат дати. Використайте формат 'YYYY-MM-DD'.")
        exit()

exchange_rate_data = converter.get_exchange_rate(date_input)

if exchange_rate_data:
    file_path = "exchange_rates.txt"
    converter.save_exchange_rate_to_file(exchange_rate_data, file_path)
    print(f"Курси валют були збережені в файлі {file_path}")

