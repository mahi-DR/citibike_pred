import pandas as pd
import lightgbm as lgb
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import os

# Set up DagsHub MLflow URI
DAGSHUB_USERNAME = "mahiswar"  # Replace with your DagsHub username
DAGSHUB_REPO = "citibike-prediction"  # Replace with your DagsHub repository name
DAGSHUB_TOKEN = "d7d9f484e3a62e7008860874aeae551b77226cec"  # Replace with your DagsHub token

# Set the tracking URI for MLflow
mlflow.set_tracking_uri(f"https://dagshub.com/{DAGSHUB_USERNAME}/{DAGSHUB_REPO}.mlflow")

# Set up experiment
experiment_name = "cbtpsc-experiments"  # Experiment name
mlflow.set_experiment(experiment_name)

# Load the data
def load_data(file_path):
    print(f"📥 Loading data from {file_path} ...")
    df = pd.read_csv(
        file_path,
        dtype={
            'start_station_id': str,
            'end_station_id': str,
            'ride_id': str,
            'rideable_type': str,
            'start_station_name': str,
            'end_station_name': str,
            'member_casual': str
        },
        parse_dates=['started_at', 'ended_at'],
        low_memory=False,
    )
    df.columns = df.columns.str.strip()
    print("✅ Data loaded. Columns:", df.columns.tolist())
    return df

# Create 28-day lag features
def create_lag_features(df, days=28):
    print(f"🧼 Creating {days}-day lag features...")
    df['pickup_date'] = df['started_at'].dt.date
    df = df.sort_values(by=['start_station_name', 'pickup_date'])
    
    # Create lag features (shift the trip_duration for past 'days' days)
    for i in range(1, days + 1):
        df[f'lag_{i}'] = df.groupby('start_station_name')['trip_duration'].shift(i)

    df.dropna(inplace=True)  # Drop rows with missing lag values
    print(f"✅ Created {days}-day lag features.")
    return df

# Train the LightGBM model and log to MLflow
def log_lgbm_model(df):
    print("🧑‍💻 Training LightGBM model...")

    # Create lag features
    df_with_lags = create_lag_features(df, days=28)

    # Select features (lags)
    feature_cols = [f'lag_{i}' for i in range(1, 29)]

    X = df_with_lags[feature_cols]
    y = df_with_lags['trip_duration']

    # Split data into train/test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train LightGBM model
    model = lgb.LGBMRegressor()
    model.fit(X_train, y_train)

    # Predict and calculate MAE
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    print(f"Model MAE: {mae}")

    # Log the model and its metrics in MLflow
    with mlflow.start_run():
        mlflow.log_metric("mae_lgbm", mae)
        mlflow.log_param("model", "LightGBM")
        mlflow.sklearn.log_model(model, "lgbm_model")

    print("✅ LightGBM model logged in MLflow")

    # Extract Experiment ID and Run ID
    experiment_id = mlflow.get_experiment_by_name(experiment_name).experiment_id
    run_id = mlflow.active_run().info.run_id

    # Print the Experiment ID and Run ID
    print(f"Experiment ID: {experiment_id}")
    print(f"Run ID: {run_id}")
    
    return model, mae  # Ensure the model and mae are returned

# Main function to run everything
def main():
    # Set up the file path for your CSV file (replace with your actual path)
    input_csv = "/content/202504-citibike-tripdata_4.csv"  # Adjust this path to your file location

    # Load and preprocess the data
    df = load_data(input_csv)
    
    # Train and log the LightGBM model
    model, mae = log_lgbm_model(df)

    print("✅ Pipeline finished!")

# Run everything
if __name__ == "__main__":
    main()
