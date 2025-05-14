from fastapi import FastAPI
from pydantic import BaseModel
from database import get_recommendations

app = FastAPI()

class RecommendationRequest(BaseModel):
    genre: str | None = None
    min_rating: float = 4.0
    n: int = 10

@app.post("/recommend")
async def recommend(request: RecommendationRequest):
    recommendations = get_recommendations(
        genre=request.genre,
        min_rating=request.min_rating,
        n=request.n
    )
    return {"recommendations": recommendations}
