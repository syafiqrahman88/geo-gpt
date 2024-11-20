import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def analyze_with_gpt(data):
    openai.api_key = os.getenv('OPENAI_API_KEY')  # Get the OpenAI API key from environment variables

    prompt = f"""
    Analyze the following website data for SEO improvements:
    Title: {data['title']}
    Description: {data['description']}
    Headers: {data['headers']}
    Paragraphs: {data['paragraphs']}
    
    Provide suggestions for SEO structure, content optimization, engagement boosters, and user experience.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['choices'][0]['message']['content']
