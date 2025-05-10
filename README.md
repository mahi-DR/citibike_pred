# Citi Bike Trip Prediction System

## Overview
This project implements a prediction system for Citi Bike trip data. The system processes raw trip data, trains models, and serves predictions. It uses Hopsworks for feature storage, MLflow for experiment tracking, and Streamlit for the frontend.

## Steps:
1. **Data Engineering**: Fetch raw Citi Bike data, clean, and preprocess it.
2. **Modeling & Experiment Tracking**: Log and track models in MLflow.
3. **Automation**: Use GitHub Actions for feature engineering, inference, and model training.
4. **Frontend & Monitoring**: Build a prediction app and model monitoring app using Streamlit.

## Setup:
1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Set up Hopsworks and DagsHub API keys.
4. Run the workflows via GitHub Actions.

## License
This project is licensed under the MIT License.
