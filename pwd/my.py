import streamlit as st
import random
import string

def generate_password(lenght, use_digits, use_special):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(lenght))

st.title("Password Generator")

length = st.slider("select password length", min_value=6, max_value=32, value=12)

use_digits = st.checkbox("include digits")
use_special = st.checkbox("include special characters")

if st.button("generate password"):
    password = generate_password(length, use_digits, use_special)
    st.success(f"generated password: `{password}`")

st.write("---")
st.write("made with ❤️ by [Muhmmad Mustafa](https://github.com/mustafa861)")