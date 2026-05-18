import requests
api_key = "04b7a15459f292d884f2098ee272e56b"

def get_atmospheric_data(city=''):
    link = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(link)
    data = response.json()
    # print(data)
    # print("Country - ", data["sys"]["country"])
    # print("City - ", data["name"])
    # print("Description - ", data["weather"][0]["description"])
    # print("Timezone - ", data["timezone"])
    # print("Temp - ", data["main"]["temp"])
    # print("Humidity - ", data["main"]["humidity"])
    return "Today's Weather:", data["main"]["temp"] ,data["weather"][0]["description"]

city = "Shimla"
get_atmospheric_data(city)