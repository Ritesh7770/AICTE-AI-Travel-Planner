import requests

def get_location_info(destination):
    """Fetch basic location data using OpenStreetMap API (with error handling)."""
    try:
        if not destination.strip():
            return {"error": "No destination provided"}

        url = f"https://nominatim.openstreetmap.org/search?q={destination}&format=json"
        headers = {"User-Agent": "AI-Travel-Planner/1.0"} 
        res = requests.get(url, headers=headers, timeout=10)

        
        try:
            data = res.json()
        except ValueError:
            return {"error": "Invalid response from location API"}

        if not data:
            return {"error": "Destination not found. Please enter a valid city or place name."}

        return {
            "name": data[0].get("display_name", "Unknown"),
            "lat": data[0].get("lat", "N/A"),
            "lon": data[0].get("lon", "N/A"),
        }

    except requests.RequestException as e:
        return {"error": f"Network error: {str(e)}"}