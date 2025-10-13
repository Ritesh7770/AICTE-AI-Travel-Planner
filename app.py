import streamlit as st
from backend.logic import get_travel_plan
from backend.data_handler import get_location_info

st.set_page_config(page_title="AI Travel Planner for Students", page_icon="🧭")

st.title("🧳 AI Travel Planner for Students")
st.caption("Personalized, budget-friendly itineraries powered by Gemini AI")

destination = st.text_input("🎯 Enter Destination")
budget = st.number_input("💰 Enter Budget (₹)", min_value=1000, step=500)
duration = st.number_input("🗓️ Trip Duration (days)", min_value=1, step=1)
interests = st.text_area("🌍 Your Interests (e.g., beaches, history, food):")

if st.button("✨ Generate My Itinerary"):
    if destination and budget and duration:
        with st.spinner("Planning your trip..."):
            location = get_location_info(destination)
            st.subheader("📍 Destination Info")
            st.write(location.get("name", "N/A"))
            st.write(f"Lat: {location.get('lat', 'N/A')} | Lon: {location.get('lon', 'N/A')}")

            plan = get_travel_plan(destination, budget, duration, interests)
            st.subheader("🧭 Personalized Itinerary")
            st.write(plan)
    else:
        st.warning("Please fill all fields before generating.")