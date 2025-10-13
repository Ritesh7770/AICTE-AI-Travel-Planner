from backend.gemini_engine import generate_itinerary

def get_travel_plan(destination, budget, duration, interests):
    try:
        plan = generate_itinerary(destination, budget, duration, interests)
        return plan
    except Exception as e:
        return f"Error generating itinerary: {e}"