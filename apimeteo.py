import streamlit as st
import sqlite3
import requests
from datetime import datetime
import pandas as pd
import os

# ======================
# 🧠 ANALYSE METEO
# ======================
def weather_summary(temp, wind, rain):
    if rain > 2:
        return "🌧️ Pluie probable aujourd'hui"
    if temp < 5:
        return "❄️ Froid, couvre-toi"
    if wind > 30:
        return "💨 Vent fort"
    return "🌤️ Temps stable"

# ======================
# 🌤️ TITRE
# ======================
st.title("🌤️ Météo Live PRO")

# ======================
# 🌍 VILLES
# ======================
cities = {
    "Paris": (48.8566, 2.3522),
    "Bruxelles": (50.85, 4.35),
    "Liège": (50.6333, 5.5667),
    "Namur": (50.4669, 4.8675),
    "Huy": (50.5192, 5.2328),
    "Amay": (50.5500, 5.3167)
}

city = st.selectbox("🌍 Choisir une ville", list(cities.keys()))
lat, lon = cities[city]

# ======================
# 🌦️ API METEO
# ======================
def get_weather():
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=auto"
    return requests.get(url).json()

data = get_weather()

# ======================
# 🌡️ CURRENT WEATHER
# ======================
current = data["current_weather"]

st.metric("🌡️ Température", f"{current['temperature']} °C")
st.metric("💨 Vent", f"{current['windspeed']} km/h")

st.write("🕒 Heure API :", current["time"].replace("T", " "))
st.write("🕒 Heure locale :", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# ======================
# 🧠 ANALYSE METEO (AJOUT PROPRE)
# ======================
st.subheader("🧠 Analyse météo")

df = pd.DataFrame({
    "date": data["daily"]["time"],
    "temp_max": data["daily"]["temperature_2m_max"],
    "temp_min": data["daily"]["temperature_2m_min"],
    "pluie": data["daily"]["precipitation_sum"]
})

summary = weather_summary(
    current["temperature"],
    current["windspeed"],
    df["pluie"].iloc[0]
)

st.success(summary)

# ======================
# 💾 DATABASE SQLITE
# ======================
base_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base_dir, "meteo.db")

conn = sqlite3.connect(db_path, check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS meteo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ville TEXT,
    temperature REAL,
    vent REAL,
    pluie REAL,
    date TEXT
)
""")

conn.commit()

cursor.execute("""
if "data_saved" not in st.session_state:
    cursor.execute("""
    INSERT INTO meteo (ville, temperature, vent, pluie, date)
    VALUES (?, ?, ?, ?, ?)
    """, (
        city,
        current["temperature"],
        current["windspeed"],
        df["pluie"].iloc[0],
        current["time"]
    ))
    
    conn.commit()
    st.session_state.data_saved = True
INSERT INTO meteo (ville, temperature, vent, pluie, date)
VALUES (?, ?, ?, ?, ?)
""", (
    city,
    current["temperature"],
    current["windspeed"],
    df["pluie"].iloc[0],
    current["time"]
))

conn.commit()
conn.close()

# ======================
# 📅 PREVISIONS
# ======================
st.subheader("📅 Prévisions 7 jours")
st.dataframe(df)

st.line_chart(df.set_index("date")[["temp_max", "temp_min"]])

# ======================
# 🌧️ PLUIE
# ======================
st.subheader("🌧️ Pluie aujourd'hui")
st.write(f"{df['pluie'].iloc[0]} mm")

# ======================
# 🗺️ CARTE
# ======================
st.subheader("🗺️ Carte")
st.map(pd.DataFrame({"lat": [lat], "lon": [lon]}))
