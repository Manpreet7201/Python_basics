from weather import get_atmospheric_data
from quote import get_quote_data
city = "Chandigarh"
weather = get_atmospheric_data(city)
quote = get_quote_data()
print("Good Morning ☀️")
print()
print(f"Weather in {city}: {weather}")

print()
print(f"Quote of the Day: {quote}")
