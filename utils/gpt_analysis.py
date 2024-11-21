import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def analyze_with_gpt(data):
    openai.api_key = os.getenv('OPENAI_API_KEY')  # Get the OpenAI API key from environment variables

    # Function to create a prompt for analysis
    def create_prompt(chunk):
        return f"""
        You are an expert on Search Engine Optimization (SEO) and Generative Engine Optimization (GEO). Analyze the following website data for SEO and GEO improvements:
        
        Title: {chunk['title']}
        Description: {chunk['description']}
        Headers: {chunk['headers']}
        Paragraphs: {chunk['paragraphs']}
        Broken Links: {chunk['broken_links']}
        Duplicate Content: {chunk['duplicate_content']}
        Robots.txt Content: {chunk['robots_content']}
        Sitemap Content: {chunk['sitemap_content']}
        
        For each of the following sections, provide a 'Issue' and 'Recommendation' formatted analysis, with examples where able:
        1. **GEO Structure Improvements**: Suggest changes for schema, metadata, sitemap and keyword usage that results in better inclusion in gen AI outputs.
        2. **Content Optimization**: Provide recommendations for topic clustering, clearer headings, and FAQs.
        3. **Engagement Boosters**: Recommend interactive features and personalized landing pages.
        4. **User Experience Feedback**: Give insights on readability, flow, accessibility and broken link analysis.
        5. **Generative Engine Optimization Strategies**: Suggest strategies in which website content can appear in outputs of generative AI models.
        """

    # Collect responses from the entire data without chunking
    current_chunk = {
        'title': data['title'],
        'description': data['description'],
        'headers': data['headers'],
        'broken_links': data['broken_links'],
        'duplicate_content': data['duplicate_content'],
        'robots_content': data['robots_content'],
        'sitemap_content': data['sitemap_content'],
        'paragraphs': data['paragraphs']  # Use all paragraphs
    }
    prompt = create_prompt(current_chunk)

    response = openai.ChatCompletion.create(
        model="o1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['choices'][0]['message']['content']
