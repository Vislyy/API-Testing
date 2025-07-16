import requests
import datetime

def converter_val(valcode_from, valcode_to, count):
    date_raw = str(datetime.date.today())
    date = int(date_raw.replace("-", ""))
    print(date)
    print(valcode_from)
    response_from = requests.get(f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={valcode_from}&date={date}&json")
    response_to = requests.get(f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={valcode_to}&date={date}&json")
    print(response_to.text)
    data0 = response_from.json()
    data1 = response_to.json()
    currency_from = data0[0]["rate"]
    currency_to = data1[0]["rate"]
    result = currency_from * count / currency_to
    print(result)

    return result





