# RiceVarietyVision Backend

FastAPI 기반 쌀 품종 분류 백엔드 서버

## 설치

```bash
cd backend
pip install -r requirements.txt
```

## 실행

```bash
uvicorn app.main:app --reload --port 8000
```

서버가 실행되면:
- API 문서: http://localhost:8000/docs
- 헬스 체크: http://localhost:8000/health

## API 엔드포인트

- `GET /health` - 헬스 체크
- `POST /predict` - 단일 이미지 예측
- `POST /batch` - 배치 이미지 예측
- `POST /export/xlsx` - Excel 내보내기

자세한 API 문서는 `/docs`에서 확인할 수 있습니다.
