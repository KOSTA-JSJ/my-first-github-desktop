"""
더미 예측 서비스
실제 모델이 준비되면 이 부분을 교체하면 됩니다.
"""
import random
from typing import List, Dict
from PIL import Image


# 품종 라벨
LABELS = ["백미", "현미", "흑미"]


def predict_image(image: Image.Image, filename: str) -> Dict:
    """
    이미지를 분석하여 품종을 예측합니다.
    
    Args:
        image: PIL Image 객체
        filename: 파일명
        
    Returns:
        예측 결과 딕셔너리
    """
    # 더미 예측: 랜덤하게 라벨 선택
    main_label = random.choice(LABELS)
    main_confidence = random.uniform(0.6, 0.95)
    
    # 나머지 라벨들의 confidence 생성
    remaining_confidence = 1.0 - main_confidence
    other_labels = [label for label in LABELS if label != main_label]
    
    all_predictions = [
        {"label": main_label, "confidence": round(main_confidence, 3)}
    ]
    
    # 나머지 confidence를 랜덤 분배
    for i, label in enumerate(other_labels):
        if i == len(other_labels) - 1:
            # 마지막은 남은 것을 모두 할당
            conf = round(remaining_confidence, 3)
        else:
            conf = round(random.uniform(0, remaining_confidence * 0.7), 3)
            remaining_confidence -= conf
        all_predictions.append({"label": label, "confidence": conf})
    
    # 정규화 (합이 1.0이 되도록)
    total = sum(p["confidence"] for p in all_predictions)
    for pred in all_predictions:
        pred["confidence"] = round(pred["confidence"] / total, 3)
    
    return {
        "filename": filename,
        "prediction": main_label,
        "confidence": round(main_confidence, 3),
        "all_predictions": all_predictions
    }


def predict_batch(images: List[Image.Image], filenames: List[str]) -> List[Dict]:
    """
    여러 이미지를 배치로 예측합니다.
    
    Args:
        images: PIL Image 객체 리스트
        filenames: 파일명 리스트
        
    Returns:
        예측 결과 리스트
    """
    results = []
    for image, filename in zip(images, filenames):
        result = predict_image(image, filename)
        results.append(result)
    return results
