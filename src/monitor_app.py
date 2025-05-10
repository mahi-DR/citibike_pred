import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import random

# Function to generate trip duration
def predict_trip_duration(start_station, end_station, rideable_type):
    if start_station == end_station:
        return 0.0
    return round(random.uniform(4, 10), 2)

# Streamlit App for Monitoring Model Predictions
def main():
    st.title("Mock Citi Bike Trip Duration Predictor")

    st.markdown("### Enter the trip details:")

    # Dropdowns for selecting trip details
    start_station = st.selectbox("Start Station", [
        "Sterling Pl & Franklin Ave", "Caton Ave & Bedford Ave", "Ocean Ave & Crooke Ave", 
        "Broadway & W 41 St", "St Marks Pl & 2 Ave", "Isham St & Broadway", "Dyckman St & Staff St", 
        "W 111 St & 5 Ave", "W 52 St & 5 Ave", "Rogers Ave & Sterling St", "Court St & State St", 
        "4488.08 Adams St & Prospect St", "President St & 4 Ave", "4101.17 E 1 St & Bowery", 
        "Underhill Ave & Pacific St", "Prospect Pl & Underhill Ave", "Ave & W 131 St", "W54 St & 11 Ave"
    ])
    end_station = st.selectbox("End Station", [
        "Sterling Pl & Franklin Ave", "Caton Ave & Bedford Ave", "Ocean Ave & Crooke Ave", 
        "Broadway & W 41 St", "St Marks Pl & 2 Ave", "Isham St & Broadway", "Dyckman St & Staff St", 
        "W 111 St & 5 Ave", "W 52 St & 5 Ave", "Rogers Ave & Sterling St", "Court St & State St", 
        "4488.08 Adams St & Prospect St", "President St & 4 Ave", "4101.17 E 1 St & Bowery", 
        "Underhill Ave & Pacific St", "Prospect Pl & Underhill Ave", "Ave & W 131 St", "W54 St & 11 Ave"
    ])
    rideable_type = st.selectbox("Rideable Type", ["Classic Bike", "Electric Bike"])

    if st.button("Predict Trip Duration"):
        # Predict the duration
        predicted_duration = predict_trip_duration(start_station, end_station, rideable_type)
        st.success(f"Predicted Trip Duration: {predicted_duration} minutes")

        # Add the prediction data to a DataFrame to simulate saving to a model monitoring log
        if 'predictions' not in st.session_state:
            st.session_state['predictions'] = pd.DataFrame(columns=["Start Station", "End Station", "Rideable Type", "Predicted Duration"])

        # Add new prediction to the session state
        new_prediction = pd.DataFrame({
            "Start Station": [start_station],
            "End Station": [end_station],
            "Rideable Type": [rideable_type],
            "Predicted Duration": [predicted_duration]
        })
        st.session_state['predictions'] = pd.concat([st.session_state['predictions'], new_prediction], ignore_index=True)

        # Display the updated predictions table
        st.write("Predictions History:")
        st.dataframe(st.session_state['predictions'])

        # Plot the trip duration over time (or number of model runs)
        plt.plot(st.session_state['predictions']["Predicted Duration"])
        plt.title("Trip Duration Over Time")
        plt.xlabel("Prediction Run Number")
        plt.ylabel("Predicted Trip Duration (minutes)")
        st.pyplot()

if __name__ == "__main__":
    main()
