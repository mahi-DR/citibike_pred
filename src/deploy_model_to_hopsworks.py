# src/deploy_model_to_hopsworks.py
import mlflow
import mlflow.sklearn
import hopsworks

def register_model_in_hopsworks(model, model_name="LightGBM", project_name="citibikes_pred"):
    try:
        # Log into the Hopsworks project
        project = hopsworks.login(api_key_value="WcQh11Y4g9GujrSD.nq14GZriFX54wIyUD22JGD3OMjbQolCgwPXpcfXMYmd4VvyCUXT5WEBc7pxr70dD", project=project_name)
        print(f"✅ Logged into Hopsworks project: {project.name}")

        # Get the model registry
        model_registry = project.get_model_registry()

        # Create a new model version (if needed)
        model_version = model_registry.create_model_version(
            model_name=model_name,
            model=model
        )
        print(f"✅ Model '{model_name}' registered successfully with version {model_version.version}")
        
    except Exception as e:
        print(f"❌ Error registering model: {e}")

def deploy_model_for_inference(model_name="LightGBM", project_name="citibikes_pred"):
    try:
        # Log into the Hopsworks project
        project = hopsworks.login(api_key_value="WcQh11Y4g9GujrSD.nq14GZriFX54wIyUD22JGD3OMjbQolCgwPXpcfXMYmd4VvyCUXT5WEBc7pxr70dD", project=project_name)
        print(f"✅ Logged into Hopsworks project: {project.name}")

        # Get the model registry and retrieve the model
        model_registry = project.get_model_registry()
        model = model_registry.get_model(model_name)
        print(f"✅ Model '{model_name}' retrieved for inference.")
        
        # Deploy the model (use in your inference pipeline)
        # Here you can create a function to deploy the model for serving predictions.

    except Exception as e:
        print(f"❌ Error deploying model: {e}")

# Example usage
if __name__ == "__main__":
    model = mlflow.sklearn.load_model("models/lgbm_model")
    register_model_in_hopsworks(model, model_name="LightGBM", project_name="citibikes_pred")
    deploy_model_for_inference(model_name="LightGBM", project_name="citibikes_pred")
