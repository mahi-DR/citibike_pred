
import streamlit as st
import pandas as pd
import mlflow
import mlflow.sklearn
import lightgbm as lgb

# Load the trained model from Hopsworks/MLflow
def load_model():
    run_id = "757049af1f524840ba2d9c30afd32566"  # Your Run ID here
    model = mlflow.sklearn.load_model(f"runs:/{run_id}/model")  # Load model from the specific run
    return model

# Function to make predictions
def make_predictions(model, features):
    predictions = model.predict([features])
    return predictions

# Streamlit UI
def main():
    st.title("Citi Bike Trip Duration Prediction")

    st.markdown("Enter the details of the bike trip:")

    # User inputs for prediction (example: pickup and drop-off data)
    start_station = st.selectbox("Start Station", ["Station 1", "Station 2", "Station 3"])  # Add real stations
    rideable_type = st.selectbox("Rideable Type", ["Classic Bike", "Electric Bike"])

    trip_duration = st.number_input("Trip Duration (Minutes)", min_value=0)

    # When the user clicks the "Predict" button
    if st.button("Predict"):
        model = load_model()  # Load the trained model

        # Example feature vector - in practice, you should map the inputs to your feature vector
        features = [start_station, rideable_type, trip_duration]
        
        prediction = make_predictions(model, features)
        st.write(f"Predicted Trip Duration: {prediction[0]:.2f} minutes")

if __name__ == "__main__":
    main()
