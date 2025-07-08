from main import get_coordinates, analyze_city
import streamlit as st
import asyncio

st.title("Weather App for Many Countries - Julian!")
city = st.text_input("What is your city?").strip().lower()

if st.button("Get Weather"):
    try:
        coordinates = asyncio.run(get_coordinates(city))
        latitude, longitude, city = coordinates
        if latitude and longitude:
            temp, wind, direction = asyncio.run(analyze_city(latitude, longitude))
            st.subheader(f"Weather in {city.title()}")
            st.write(f"**Temperature:** {temp}°C")
            st.write(f"**Windspeed:** {wind} km/h")
            st.write(f"**Wind Direction:** {direction}°")
        else:
            st.error("City not found. Please try again.")
    except:
        st.error("City not found. Please try again.")