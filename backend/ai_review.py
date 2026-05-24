import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def review_code(code):

    prompt = f"""
    You are a senior software engineer.

    Review this code and find:
    1. Bugs
    2. Security issues
    3. Performance problems
    4. Best practice violations

    Give output in bullet points.

    Code:
    {code}
    """

    response = model.generate_content(prompt)

    return response.text