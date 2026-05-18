import requests

def get_quote_data():
    link = f"https://zenquotes.io/api/today"

    response = requests.get(link)
    data = response.json()
    quote = data[0]["q"]
    author = data[0]["a"]
    # print("Quote of the Day:")
    return quote,"-",author
    # print("Country - ", data["sys"]["country"])
    # print("City - ", data["name"])
    # print("Description - ", data["weather"][0]["description"])
    # print("Timezone - ", data["timezone"])
    # print("Temp - ", data["main"]["temp"])
    # print("Humidity - ", data["main"]["humidity"])

get_quote_data()