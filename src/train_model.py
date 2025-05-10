import pandas as pd
import lightgbm as lgb
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

def train_model(df):
    X = df.drop(columns=['trip_duration', 'ride_id'])
    y = df['trip_duration']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = lgb.LGBMRegressor()
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    
    mlflow.log_metric("mae", mae)
    mlflow.sklearn.log_model(model, "lgbm_model")
    
    return model, mae

def main():
    df = pd.read_csv("data/processed_data/processed_data.csv")
    model, mae = train_model(df)
    print(f"Model MAE: {mae}")

if __name__ == "__main__":
    main()
