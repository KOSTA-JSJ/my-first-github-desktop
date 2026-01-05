# API Documentation
## RiceVarietyVision Backend API

### Base URL
```
http://localhost:8000
```

### Endpoints

#### 1. Health Check
```
GET /health
```

**Response:**
```json
{
  "status": "healthy",
  "version": "1.0.0"
}
```

---

#### 2. Single Image Prediction
```
POST /predict
Content-Type: multipart/form-data
```

**Request:**
- `file`: 이미지 파일 (multipart/form-data)

**Response:**
```json
{
  "filename": "rice_image.jpg",
  "prediction": "백미",
  "confidence": 0.85,
  "all_predictions": [
    {"label": "백미", "confidence": 0.85},
    {"label": "현미", "confidence": 0.10},
    {"label": "흑미", "confidence": 0.05}
  ]
}
```

---

#### 3. Batch Prediction
```
POST /batch
Content-Type: multipart/form-data
```

**Request:**
- `files`: 이미지 파일 배열 (multipart/form-data)

**Response:**
```json
{
  "results": [
    {
      "filename": "rice1.jpg",
      "prediction": "백미",
      "confidence": 0.85,
      "all_predictions": [...]
    },
    {
      "filename": "rice2.jpg",
      "prediction": "현미",
      "confidence": 0.92,
      "all_predictions": [...]
    }
  ],
  "total": 2
}
```

---

#### 4. Export to Excel
```
POST /export/xlsx
Content-Type: application/json
```

**Request:**
```json
{
  "results": [
    {
      "filename": "rice1.jpg",
      "prediction": "백미",
      "confidence": 0.85
    },
    {
      "filename": "rice2.jpg",
      "prediction": "현미",
      "confidence": 0.92
    }
  ]
}
```

**Response:**
- Content-Type: `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`
- 파일 다운로드 (Excel .xlsx)

**Excel 형식:**
- 컬럼: 파일명, 예측 품종, 신뢰도
- 신뢰도 기반 조건부 서식:
  - 높음 (≥0.8): 녹색
  - 중간 (0.5-0.8): 노란색
  - 낮음 (<0.5): 빨간색
