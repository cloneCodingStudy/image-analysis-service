import os
import google.generativeai as genai
from dotenv import load_dotenv

# .env 파일 로드 (환경 변수를 사용할 때)
load_dotenv()

# 환경 변수에서 API_KEY를 불러옵니다.
api_key = os.getenv("API_KEY")

# Google Generative AI 설정 및 모델 호출
def generate_content_from_image(image_path: str):
    # 모델 설정 (API 키 및 모델 지정)
    genai.configure(api_key=api_key)  # 환경 변수로 API 키 사용
    model = genai.GenerativeModel("models/gemini-2.5-flash")

    # 이미지 파일 업로드
    file = genai.upload_file(image_path)

    # 프롬프트 생성
    prompt = (
        "이 이미지를 보고 사진 속 물건을 인식해서 대여 게시글 정보를 만들어줘.\n"
        "결과는 반드시 JSON 형식으로, 아래 예시처럼 반환해.\n\n"
        "{\n"
        "  \"title\": \"물건 이름 + 특징\",\n"
        "  \"description\": \"물건에 대한 간단한 설명\",\n"
        "  \"price\": 숫자 (하루 기준 원 단위),\n"
        "  \"condition\": \"상태 설명 (예: 새것 같음, 사용감 있음 등)\",\n"
        "}\n\n"
        "가격은 5,000~50,000원 사이로 합리적으로 제안해줘."
    )

    # 모델로부터 결과 받기
    result = model.generate_content([prompt, file])
    return result.text.strip()
