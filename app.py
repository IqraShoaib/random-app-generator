import streamlit as st
import requests
import random

st.set_page_config(page_title="Random Quote Generator", page_icon="✨", layout="centered")

st.title("✨ Random Quote Generator")

# API for quotes
API_URL = "https://type.fit/api/quotes"

@st.cache_data
def get_quotes():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        return []

quotes = get_quotes()

if quotes:
    if st.button("Generate Quote"):
        quote = random.choice(quotes)
        st.markdown(f"### \"{quote['text']}\"")
        st.write(f"— {quote['author'] if quote['author'] else 'Unknown'}")
else:
    st.error("Failed to load quotes. Please try again later.")
