import streamlit as st
from utils.crawler import crawl_website
from utils.gpt_analysis import analyze_with_gpt
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Streamlit app title
st.title("GEO GPT Wrapper")

# User input for URL
url = st.text_input("Enter website URL")

if st.button("Analyze"):
    if url:
        data = crawl_website(url)
        if data:
            recommendations = analyze_with_gpt(data)
            st.subheader("GEO Recommendations:")
            st.write(recommendations)
        else:
            st.error("Failed to retrieve the website.")
    else:
        st.error("Please enter a valid URL.")
