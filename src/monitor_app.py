
import streamlit as st
import pandas as pd
import mlflow
import matplotlib.pyplot as plt

# Function to fetch model metrics from MLflow
def fetch_model_metrics():
    client = mlflow.tracking.MlflowClient()
    experiment_id = "0"  # Replace with your actual experiment ID
    runs = client.search_runs(experiment_id)

    metrics = []
    for run in runs:
        metrics.append({
            "run_id": run.info.run_id,
            "mae": run.data.metrics.get("mae_lgbm", None)
        })

    df_metrics = pd.DataFrame(metrics)
    return df_metrics

# Streamlit UI
def main():
    st.title("Model Monitoring Dashboard")

    st.markdown("Here you can monitor the performance of the deployed model.")

    # Fetch metrics
    df_metrics = fetch_model_metrics()

    if df_metrics.empty:
        st.write("No metrics found.")
    else:
        st.write("Model Performance (MAE):")
        st.dataframe(df_metrics)

        # Plot MAE over time (or number of model runs)
        plt.plot(df_metrics["mae"])
        plt.title("Model MAE over Time")
        plt.xlabel("Run Number")
        plt.ylabel("Mean Absolute Error (MAE)")
        st.pyplot()

if __name__ == "__main__":
    main()
