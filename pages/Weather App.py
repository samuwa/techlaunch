import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

# Set page configuration
st.set_page_config(page_title="Weather App Demo", layout="wide")

# App Title & Description
st.subheader("Weather App Demo")

col1, col2, col3 = st.columns([6,1,2])
col1.write(
    """
    This app shows how we can use [Open-Meteo](https://open-meteo.com/) (a free weather **API**)
    to fetch hour-by-hour temperature data for a selected city and time period.
    """)

popover = col3.popover("What is an **API**?")
popover.info('An API, or Application Programming Interface, is a "bridge" that programmers build so other programmers (like us!) can use the tools they created.')


st.write("""
    Through :blue[**TechLaunch**], you'll learn how to do similar things: 
    connecting Python to different services, tools, and code created by other people 
    so you can build your own projects quickly!
    """
)


st.markdown("#")
# 1. Choose a city from predefined lat/lon coordinates
city_coords = {
    "Panama City": (8.983333, -79.516670),
    "London": (51.5074, -0.1278),
    "New York": (40.7128, -74.0060),
    "Tokyo": (35.6895, 139.6917)
}

city = st.selectbox("Select a city to view its forecast:", list(city_coords.keys()))

# 2. Use a slider to determine how many days ahead to forecast
days = st.slider("How many days of forecast data would you like to see?", 1, 7, 3)

# Extract chosen city's coordinates
lat, lon = city_coords[city]

# Calculate the end date (today + days)
start_date = datetime.utcnow().date()  # today's date (UTC)
end_date = start_date + timedelta(days=days)

# Open-Meteo requires dates in YYYY-MM-DD format
start_date_str = start_date.strftime("%Y-%m-%d")
end_date_str = end_date.strftime("%Y-%m-%d")

# 3. Fetch the weather data from Open-Meteo (hourly temperatures)
url = (
    "https://api.open-meteo.com/v1/forecast"
    f"?latitude={lat}&longitude={lon}"
    f"&hourly=temperature_2m"
    f"&start_date={start_date_str}"
    f"&end_date={end_date_str}"
    "&timezone=UTC"  # Force UTC to simplify times
)

response = requests.get(url)
if response.status_code != 200:
    st.error("There was an error fetching the weather data. Please try again later.")
    st.stop()

data = response.json()

# Extract time and temperature arrays
times = data["hourly"]["time"]
temps = data["hourly"]["temperature_2m"]

# 4. Build a DataFrame for Plotly
df = pd.DataFrame({"time": times, "temperature (°C)": temps})
df["time"] = pd.to_datetime(df["time"])

# 5. Create a Plotly line chart
fig = px.line(
    df,
    x="time",
    y="temperature (°C)",
    title=f"Hourly Temperature Forecast in {city} (Next {days} Days)"
)

# Display the chart in Streamlit
st.plotly_chart(fig, use_container_width=True)

st.write(
    """
    **Pro Tip**: Adjust the slider to change the date range for the forecast. 
    Notice how the chart automatically updates to show the new date range. 
    """
)
