import requests

user_money = int(input("Введіть кількість ваших грошей у гривнях: "))
valcode = input("Введіть валюту: ")
date = input("Введіть дату: ")

response = requests.get(f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={valcode}&date={date}&json")

print(response.status_code)
data = response.json()

user_converted_money = user_money / data[0]["rate"]
price = data[0]["rate"]
date = data[0]["exchangedate"]

print(f"Валюта: {valcode}")
print(f"Ціна: {round(price)}")
print(f"Дата: {date}")
print(f"В вас є {round(user_converted_money)} {valcode}")