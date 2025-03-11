import streamlit as st
import random
import time
import requests

st.title("💰 Money Making Machine")

def generate_money():
    """Generates a random amount of money between $1 and $1000"""
    return random.randint(1, 1000)

st.subheader("💸 Instant Cash Generator")
if st.button("Generate Money"):
    st.write("⏳ Counting your money...")
    time.sleep(1)  # Simulates delay
    amount = generate_money()
    st.success(f"🎉 You made **${amount}**!")

# Fetch Side Hustle from FastAPI
def fetch_side_hustle():
    try:
        response = requests.get("http://127.0.0.1:8000/side_hustles?apiKey=1234567890")
        if response.status_code == 200:
            data = response.json()
            return data.get("side_hustle", "Freelancing")
        else:
            return "Couldn't fetch hustle idea. Try again!"
    except requests.exceptions.RequestException:
        return "🚨 Server error! Make sure FastAPI is running."

st.subheader("💼 Side Hustle Ideas")
if st.button("Generate Hustle"):
    idea = fetch_side_hustle()
    st.success(f"🚀 **{idea}**")
