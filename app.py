import streamlit as st
from utils.crawler import crawl_website
from utils.gpt_analysis import analyze_with_gpt
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Streamlit app title
st.title("Sequencr Consulting GEO Analyzer")

# User input for URL
url = st.text_input("Enter website URL")

if st.button("Analyze"):
    if url:
        # Step 1: Crawl the website
        data = crawl_website(url)
        if data:
            # Step 2: Analyze the data with GPT without chunking
            recommendations = analyze_with_gpt(data)
            st.subheader("GEO Recommendations:")
            st.write(recommendations)  # Display the recommendations
        else:
            st.error("Failed to retrieve the website.")
    else:
        st.error("Please enter a valid URL.")
