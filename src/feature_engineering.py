import pandas as pd
import hopsworks
from hsfs.feature import Feature
import os

API_KEY = "WcQh11Y4g9GujrSD.nq14GZriFX54wIyUD22JGD3OMjbQolCgwPXpcfXMYmd4VvyCUXT5WEBc7pxr70dD"
PROJECT_NAME = "citibikes_pred"
FEATURE_GROUP_NAME = "cbtpsc_cleaned_v1"
INPUT_CSV = "data/raw_data/citibike_tripdata.csv"

def load_data(file_path):
    df = pd.read_csv(file_path)
    # Preprocessing and feature extraction logic
    return df

def store_data_in_hopsworks(df, api_key_value, project_name, feature_group_name):
    project = hopsworks.login(api_key_value=api_key_value, project=project_name)
    fs = project.get_feature_store()
    features = [Feature("ride_id", "string"), Feature("rideable_type", "string"), Feature("trip_duration", "double")]
    fg = fs.create_feature_group(name=feature_group_name, version=1, features=features)
    fg.insert(df)

def main():
    df = load_data(INPUT_CSV)
    store_data_in_hopsworks(df, API_KEY, PROJECT_NAME, FEATURE_GROUP_NAME)

if __name__ == "__main__":
    main()
