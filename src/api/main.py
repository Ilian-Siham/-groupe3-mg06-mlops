from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from src.Model.ModelPrediction import Build_semantic_model
from src.Database.Data_pipeline import run_data_user_pipeline

app = FastAPI()

# Input for API and model status
@app.get("/health")
def health():
    return {"status": "model_loaded", "service": "active"}

# Input point for prediction
@app.post("/predict")
def predict():

    # Call the data pipeline for user questionary
    run_data_user_pipeline()

    # Call the model prediction
    df_comp, df_byjob = Build_semantic_model()

    # Convert DataFrames to JSON
    result = {
        "job_matches": jsonable_encoder(df_byjob.to_dict(orient="records")),
        "skills_details": jsonable_encoder(df_comp.to_dict(orient="records"))
    }
    return result
