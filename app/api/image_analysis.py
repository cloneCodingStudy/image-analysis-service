from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.image_service import analyze_image
from app.models.rental_post import RentalPost

router = APIRouter()

@router.post("/analyze")
async def analyze_item(image: UploadFile = File(...)):
    try:
        # 이미지 분석 서비스 호출
        post_data = await analyze_image(image)

        return {"rental_post": post_data}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
