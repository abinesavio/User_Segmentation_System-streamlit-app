import streamlit as st
import pandas as pd

# Function to read and display CSV file
def read_and_display_csv(file):
    df = pd.read_csv(file)
    
    # Display first 5 observations
    st.write("First 5 observations:")
    st.write(df.head())

    # Add a "PREDICT" button
    if st.button("PREDICT"):
        # Add your prediction logic here
        st.write("Prediction logic goes here...")

# Title for the Streamlit app
st.title("USER SEGMENTATION SYSTEM")

# Upload CSV file through Streamlit
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:
    # Call the function to read and display CSV file
    read_and_display_csv(uploaded_file)
