import streamlit as st
import random

# List of actual station names
stations = [
    "Sterling Pl & Franklin Ave", "Caton Ave & Bedford Ave",
    "Ocean Ave & Crooke Ave", "Broadway & W 41 St", "St Marks Pl & 2 Ave",
    "Isham St & Broadway", "Dyckman St & Staff St", "W 111 St & 5 Ave",
    "W 52 St & 5 Ave", "Rogers Ave & Sterling St", "Court St & State St",
    "4488.08 Adams St & Prospect St", "President St & 4 Ave",
    "4101.17 E 1 St & Bowery", "Underhill Ave & Pacific St",
    "Prospect Pl & Underhill Ave", "Ave & W 131 St", "W54 St & 11 Ave"
]

# Function to generate trip duration
def predict_trip_duration(start_station, end_station, rideable_type):
    if start_station == end_station:
        return 0.0
    return round(random.uniform(4, 10), 2)

# Streamlit App
def main():
    st.title("Mock Citi Bike Trip Duration Predictor")

    st.markdown("### Enter the trip details:")

    start_station = st.selectbox("Start Station", stations)
    end_station = st.selectbox("End Station", stations)
    rideable_type = st.selectbox("Rideable Type", ["Classic Bike", "Electric Bike"])

    if st.button("Predict Trip Duration"):
        predicted_duration = predict_trip_duration(start_station, end_station, rideable_type)
        st.success(f"Predicted Trip Duration: {predicted_duration} minutes")

if __name__ == "__main__":
    main()
