import pandas as pd
import mlflow
import lightgbm as lgb

def load_model():
    model = mlflow.sklearn.load_model("models/lgbm_model")
    return model

def make_predictions(model, df):
    predictions = model.predict(df)
    df['predictions'] = predictions
    return df

def main():
    df = pd.read_csv("data/processed_data/processed_data.csv")
    model = load_model()
    df_with_predictions = make_predictions(model, df)
    df_with_predictions.to_csv("data/inference_results/inference_results.csv", index=False)

if __name__ == "__main__":
    main()
