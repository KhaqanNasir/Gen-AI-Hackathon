import streamlit as st

# Set up Streamlit page config (must be the first Streamlit command)
st.set_page_config(
    page_title="Testing | Page 02",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Page content
st.title("Page 02: Testing")
st.write("Welcome to Page 02! This is a testing page.")
