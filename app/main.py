from fastapi import FastAPI
from .api import image_analysis

app = FastAPI()

# 이미지 분석 API 라우팅
app.include_router(image_analysis.router)
