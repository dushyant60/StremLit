import streamlit as st

# Title of your app
st.title("Welcome to My First Streamlit App!")

# Add some text
st.write("Here, you can do amazing things!")

# Add a slider
number = st.slider("Choose a number", 0, 100)

# Show the selected number
st.write(f"You selected: {number}")
