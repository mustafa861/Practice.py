import streamlit as st
import pandas as pd
import numpy as np

# Set page title and configuration
st.set_page_config(page_title="My Streamlit App", layout="wide")

# Add a title
st.title("Welcome to My Streamlit App!")

# Add a sidebar
st.sidebar.header("Sidebar Controls")

# Add some interactive elements
name = st.text_input("Enter your name:", "")
if name:
    st.write(f"Hello, {name}!")

# Add a slider
age = st.slider("Select your age:", 0, 100, 25)
st.write(f"You selected: {age} years old")

# Create two columns
col1, col2 = st.columns(2)

# Add content to first column
with col1:
    st.header("Column 1")
    if st.button("Generate Random Numbers"):
        numbers = np.random.randn(10)
        st.write("Random numbers:", numbers)

# Add content to second column
with col2:
    st.header("Column 2")
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['A', 'B', 'C']
    )
    st.line_chart(chart_data)

# Add a file uploader
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    st.write("File uploaded successfully!")
