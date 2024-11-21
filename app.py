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
            # Step 2: Chunk the paragraphs before analysis
            max_paragraph_length = 2000  # Adjust this value based on your needs
            paragraphs = data['paragraphs']
            chunks = []
            current_chunk = []

            for paragraph in paragraphs:
                # Check if adding the next paragraph exceeds the max length
                if len(' '.join(current_chunk + [paragraph])) > max_paragraph_length:
                    chunks.append(current_chunk)  # Save the current chunk
                    current_chunk = [paragraph]  # Start a new chunk
                else:
                    current_chunk.append(paragraph)  # Add to the current chunk

            # Add the last chunk if it exists
            if current_chunk:
                chunks.append(current_chunk)

            # Update data with chunked paragraphs
            data['paragraphs'] = chunks

            # Step 3: Analyze the data with GPT
            recommendations = analyze_with_gpt(data)
            st.subheader("GEO Recommendations:")
            st.write(recommendations)  # Display the recommendations
        else:
            st.error("Failed to retrieve the website.")
    else:
        st.error("Please enter a valid URL.")
