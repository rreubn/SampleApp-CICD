# app.py
import streamlit as st
import random

st.set_page_config(page_title="Random Number Generator", page_icon="🎲", layout="centered")

st.title("🎲 Random Number Generator")
st.write("Click the button to generate a random number!")

# Slider for range
min_val = st.slider("Minimum value:", 0, 100, 0)
max_val = st.slider("Maximum value:", 0, 100, 50)

if min_val > max_val:
    st.error("Minimum cannot be greater than maximum!")
else:
    if st.button("Generate Random Number"):
        number = random.randint(min_val, max_val)
        st.success(f"Your random number is: {number}")

# Add some colorful styling
st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #4CAF50;
    color: white;
    height: 50px;
    width: 200px;
    font-size: 20px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)
