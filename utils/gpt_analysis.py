import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def analyze_with_gpt(data):
    openai.api_key = os.getenv('OPENAI_API_KEY')  # Get the OpenAI API key from environment variables

    prompt = f"""
    Analyze the following website data for SEO and Generative Engine Optimization (GEO) improvements:
    
    Title: {data['title']}
    Description: {data['description']}
    Headers: {data['headers']}
    Paragraphs: {data['paragraphs']}
    Broken Links: {data['broken_links']}
    Duplicate Content: {data['duplicate_content']}
    Robots.txt Content: {data['robots_content']}
    Sitemap Content: {data['sitemap_content']}
    
    For each of the following sections, provide a 'Issue' and 'Recommendation' analysis:
    1. **GEO Structure Improvements**: Suggest changes for schema, metadata, and keyword usage that can lead to better inclusion in generativeAI outputs.
    2. **Content Optimization**: Provide recommendations for topic clustering, clearer headings, and FAQs.
    3. **Engagement Boosters**: Recommend interactive features and personalized landing pages.
    4. **User Experience Feedback**: Give insights on readability, flow, and accessibility.
    5. **Generative Engine Optimization Strategies**: Suggest strategies in which website content can appear in outputs of generative AI models.

    Format your response clearly, indicating the 'Issue' and 'Recommendation' for each section, with examples where appropriate.
    Add analysis of Title, Description, Headers, Paragraphs, Broken Links, Duplicate Content, Robots.txt Content, Sitemap Content at the bottom where applicable.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['choices'][0]['message']['content']
