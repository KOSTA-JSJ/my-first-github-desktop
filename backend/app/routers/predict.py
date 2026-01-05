from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from PIL import Image
from io import BytesIO
from app.models import SinglePredictionResponse, BatchPredictionResponse
from app.services.predictor import predict_image, predict_batch

router = APIRouter()


@router.post("/predict", response_model=SinglePredictionResponse)
async def predict_single(file: UploadFile = File(...)):
    """단일 이미지 예측"""
    try:
        # 이미지 읽기
        contents = await file.read()
        image = Image.open(BytesIO(contents))
        
        # RGB로 변환 (RGBA 등 대응)
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        # 예측 수행
        result = predict_image(image, file.filename)
        
        return result
    except Exception as e:
        return JSONResponse(
            status_code=400,
            content={"error": f"이미지 처리 중 오류 발생: {str(e)}"}
        )


@router.post("/batch", response_model=BatchPredictionResponse)
async def predict_batch_endpoint(files: list[UploadFile] = File(...)):
    """배치 이미지 예측"""
    try:
        images = []
        filenames = []
        
        for file in files:
            contents = await file.read()
            image = Image.open(BytesIO(contents))
            
            # RGB로 변환
            if image.mode != 'RGB':
                image = image.convert('RGB')
            
            images.append(image)
            filenames.append(file.filename)
        
        # 배치 예측 수행
        results = predict_batch(images, filenames)
        
        return {
            "results": results,
            "total": len(results)
        }
    except Exception as e:
        return JSONResponse(
            status_code=400,
            content={"error": f"배치 처리 중 오류 발생: {str(e)}"}
        )
