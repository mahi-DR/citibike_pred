import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to fetch prediction data from CSV file
def fetch_prediction_data():
    # Try reading the CSV file if it exists
    try:
        df_predictions = pd.read_csv('../predictions.csv')  # Adjust the path if necessary
        return df_predictions
    except FileNotFoundError:
        return pd.DataFrame(columns=["Start Station", "End Station", "Rideable Type", "Predicted Duration"])

# Streamlit app to monitor the predictions
def main():
    st.title("Model Monitoring Dashboard")

    st.markdown("### Monitor the predicted trip durations from the model:")

    # Fetch the prediction data from the CSV file
    df_predictions = fetch_prediction_data()

    if df_predictions.empty:
        st.write("No predictions available yet.")
    else:
        st.write("Predictions History:")
        st.dataframe(df_predictions)

        # Create a figure and axes for plotting
        fig, ax = plt.subplots()
        ax.plot(df_predictions["Predicted Duration"], marker='o', linestyle='-', color='b')
        ax.set_title("Predicted Trip Duration Over Time")
        ax.set_xlabel("Prediction Run Number")
        ax.set_ylabel("Predicted Trip Duration (minutes)")

        # Display the plot
        st.pyplot(fig)

if __name__ == "__main__":
    main()
