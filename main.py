import httpx, asyncio

async def get_coordinates(chosen=''):
    async with httpx.AsyncClient() as client:
        try:
            if __name__ == "__main__":
                chosen = input("What is your city? ").lower().strip()
            url = f'https://geocoding-api.open-meteo.com/v1/search?name={chosen}&count=1'
            result = await client.get(url)
            city = result.json()["results"][0]
            return city["latitude"], city["longitude"], chosen
        except:
            print("City not found.\n")

async def analyze_city(lat, lon):
    async with httpx.AsyncClient() as client:
        url = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true'
        result = await client.get(url)
        city = result.json()["current_weather"]
        temp = city["temperature"]
        wind = city["windspeed"]
        wind_direction = city["winddirection"]
    return temp, wind, wind_direction

def display_city(city, temp, wind, wind_direction):
    print(f"\nCurrent weather in {city.title()}:")
    print(f"Temperature: {temp}°C.")
    print(f"Windspeed: {wind} km/h.")
    print(f"Wind direction: {wind_direction} degrees.")

def main():
    lat, lon, city = asyncio.run(get_coordinates())
    temp, wind, wind_direction = asyncio.run(analyze_city(lat, lon))
    #Cant use gather because the second run needs the first one to be completed in order to itself run!
    display_city(city, temp, wind, wind_direction)

if __name__ == "__main__":
    main()