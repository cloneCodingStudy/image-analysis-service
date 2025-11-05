import tempfile
import os
import re
import json
from app.core.generative_model import generate_content_from_image

async def analyze_image(image):
    suffix = os.path.splitext(image.filename)[-1] or ".jpg"
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(await image.read())
        tmp_path = tmp.name

    try:
        # 이미지를 모델에 업로드하고 결과를 받음
        result = generate_content_from_image(tmp_path)
        result = re.sub(r"^```json|```$", "", result).strip()


        # JSON 파싱 및 결과 반환
        try:
            post_data = json.loads(result)
        except json.JSONDecodeError:
            post_data = {"raw_text": result, "error": "JSON parsing failed"}

        return post_data

    except Exception as e:
        raise e
    finally:
        os.remove(tmp_path)
