import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_itinerary(destination, budget, duration, interests):
    prompt = f"""
    You are an AI travel planner for students. 
    Create a detailed {duration}-day itinerary for {destination} 
    under a budget of ₹{budget}. 
    Focus on affordable stays, food, local transport, and student-friendly experiences. 
    Interests: {interests}.
    Provide a clear day-by-day plan.
    """

    try:
        model = genai.GenerativeModel("gemini-2.5-pro")
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        try:
            model = genai.GenerativeModel("gemini-pro")
            response = model.generate_content(prompt)
            return response.text.strip()
        except Exception as e2:
            return f"Error generating itinerary: {e2}"