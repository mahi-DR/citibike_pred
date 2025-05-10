import streamlit as st
import random
import pandas as pd
import os

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

# Function to save prediction to CSV, creating the file if it doesn't exist
def save_prediction_to_csv(start_station, end_station, rideable_type, predicted_duration):
    new_prediction = {
        "Start Station": start_station,
        "End Station": end_station,
        "Rideable Type": rideable_type,
        "Predicted Duration": predicted_duration
    }
    
    # Check if the CSV file exists
    file_exists = os.path.exists('predictions.csv')
    
    # If file exists, append to it, otherwise create the file
    if file_exists:
        df_predictions = pd.read_csv('predictions.csv')
        # Instead of append(), use pd.concat() to add the new row
        df_predictions = pd.concat([df_predictions, pd.DataFrame([new_prediction])], ignore_index=True)
        df_predictions.to_csv('predictions.csv', index=False)
    else:
        # Create a new CSV file and write the first row of data
        df_predictions = pd.DataFrame([new_prediction])
        df_predictions.to_csv('predictions.csv', index=False)

# Streamlit App for Predicting Trip Duration
def main():
    st.title("Mock Citi Bike Trip Duration Predictor")

    st.markdown("### Enter the trip details:")

    start_station = st.selectbox("Start Station", stations)
    end_station = st.selectbox("End Station", stations)
    rideable_type = st.selectbox("Rideable Type", ["Classic Bike", "Electric Bike"])

    if st.button("Predict Trip Duration"):
        # Predict the trip duration
        predicted_duration = predict_trip_duration(start_station, end_station, rideable_type)
        st.success(f"Predicted Trip Duration: {predicted_duration} minutes")

        # Save the prediction to the CSV file
        save_prediction_to_csv(start_station, end_station, rideable_type, predicted_duration)

        # Display the updated predictions table from the CSV file
        df_predictions = pd.read_csv('predictions.csv')
        st.write("Predictions History:")
        st.dataframe(df_predictions)

if __name__ == "__main__":
    main()

# Save prediction to CSV file, creating it if it doesn't exist
def save_prediction_to_csv(start_station, end_station, rideable_type, predicted_duration):
    new_prediction = {
        "Start Station": start_station,
        "End Station": end_station,
        "Rideable Type": rideable_type,
        "Predicted Duration": predicted_duration
    }

    # Check if the CSV file exists
    file_exists = os.path.exists('predictions.csv')
    
    # If file exists, append to it, otherwise create the file
    if file_exists:
        df_predictions = pd.read_csv('predictions.csv')
        df_predictions = pd.concat([df_predictions, pd.DataFrame([new_prediction])], ignore_index=True)
        df_predictions.to_csv('predictions.csv', index=False)
    else:
        # If the file doesn't exist, create a new one and save the first prediction
        df_predictions = pd.DataFrame([new_prediction])
        df_predictions.to_csv('predictions.csv', index=False)

