# src/store_data_in_hopsworks.py
import hopsworks
from hsfs.feature import Feature
import pandas as pd

def store_data_in_hopsworks(df, feature_group_name, project_name, api_key_value):
    try:
        # Log in to Hopsworks project
        project = hopsworks.login(api_key_value=api_key_value, project=project_name)
        print(f"✅ Logged into Hopsworks project: {project.name}")
        
        # Get feature store
        fs = project.get_feature_store()

        # Define features (columns) in the dataset
        features = [
            Feature("ride_id", "string"),
            Feature("rideable_type", "string"),
            Feature("start_station_name", "string"),
            Feature("start_station_id", "string"),
            Feature("end_station_name", "string"),
            Feature("end_station_id", "string"),
            Feature("trip_duration", "double"),
            Feature("predictions", "double")  # Add predictions column
        ]

        # Create a feature group (FG) for storing the data
        fg = fs.create_feature_group(
            name=feature_group_name,
            version=1,
            description="Processed data with trip duration and predictions",
            primary_key=["ride_id"],  # Primary key for the feature group
            event_time="started_at",  # Use timestamp for event time (if available)
            features=features,
            online_enabled=True
        )

        # Insert the data into the feature group
        fg.insert(df, write_options={"wait_for_job": True})
        print("✅ Data inserted into Feature Group successfully.")

    except Exception as e:
        print("❌ Error inserting data into Hopsworks:", e)

# Example usage
if __name__ == "__main__":
    df = pd.read_csv("data/inference_results/inference_results.csv")  # Your inference results
    store_data_in_hopsworks(df, "cbtpsc_predictions_v1", "citibikes_pred", "WcQh11Y4g9GujrSD.nq14GZriFX54wIyUD22JGD3OMjbQolCgwPXpcfXMYmd4VvyCUXT5WEBc7pxr70dD")
