import httpx, asyncio

cities = {
    "chicago": {"lat": 41.8781, "lon": -87.6298},
    "new york": {"lat": 40.7128, "lon": -74.0060},
    "los angeles": {"lat": 34.0522, "lon": -118.2437}
}

def get_cities(cities):
    city = ''

    while city not in cities:
        city = input("What is your city? ").lower().strip()
        if city not in cities:
            print("Please enter a valid city.\n")
    
    return city

async def analyze_city(city):
    async with httpx.AsyncClient() as client:
        url = f'https://api.open-meteo.com/v1/forecast?latitude={cities[city]["lat"]}&longitude={cities[city]["lon"]}&current_weather=true'
        result = await client.get(url)
        city = result.json()["current_weather"]
        temp = city["temperature"]
        wind = city["windspeed"]
    return temp, wind

def display_city(city, temp, wind):
    print(f"\nCurrent weather in {city.title()}:")
    print(f"Temperature: {temp}°C.")
    print(f"Windspeed: {wind} km/h.")

def main():
    print(f"Current cities: {', '.join(cities.keys())}.")
    city = get_cities(cities)
    temp, wind = asyncio.run(analyze_city(city))
    display_city(city, temp, wind)

if __name__ == "__main__":
    main()