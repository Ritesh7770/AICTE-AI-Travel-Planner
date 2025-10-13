import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# List all available models
print("✅ Available Gemini Models:\n")
for model in genai.list_models():
    print(model.name)