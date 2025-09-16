
# sample: movie recommender serving sketch (FastAPI)
from fastapi import FastAPI
app = FastAPI()

@app.get("/recommend/{user_id}")
def recommend(user_id: int, k: int = 10):
    # load model, return top-k movie ids with scores
    return {"user_id": user_id, "recommendations": []}
