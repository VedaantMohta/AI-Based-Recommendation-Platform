from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.item import ItemRecommendationResponse
from app.services.recommender import get_recommendations
from app.db import get_db

router = APIRouter()

@router.get("/recommendations", response_model=ItemRecommendationResponse)
def recommend_items(user_id: int, db: Session = Depends(get_db)):
    recommendations = get_recommendations(user_id, db)
    return {"recommendations": recommendations}