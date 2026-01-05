# Architecture Document
## RiceVarietyVision

### 시스템 아키텍처

```
┌─────────────┐
│   Frontend  │  React/Next.js
│  (React)   │
└──────┬──────┘
       │ HTTP/REST
       │
┌──────▼──────┐
│   Backend   │  FastAPI
│  (FastAPI)  │
└──────┬──────┘
       │
       ├─── Model Service (미래)
       │
       └─── Excel Exporter
            (openpyxl)
```

### 디렉토리 구조

```
rice-variety-vision/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py          # FastAPI 앱
│   │   ├── models.py        # 데이터 모델
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── predictor.py # 예측 서비스 (더미)
│   │   │   └── exporter.py  # Excel 내보내기
│   │   └── routers/
│   │       ├── __init__.py
│   │       ├── health.py
│   │       ├── predict.py
│   │       └── export.py
│   ├── requirements.txt
│   └── README.md
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── FileUpload.tsx
│   │   │   ├── ResultsTable.tsx
│   │   │   └── ExportButton.tsx
│   │   ├── App.tsx
│   │   └── main.tsx
│   ├── package.json
│   └── README.md
├── docs/
│   ├── PRD.md
│   ├── ARCHITECTURE.md
│   ├── API.md
│   └── TODO.md
└── README.md
```

### 컴포넌트 설명

#### Backend
- **main.py**: FastAPI 애플리케이션 진입점
- **predictor.py**: 이미지 분류 서비스 (현재 더미)
- **exporter.py**: Excel 파일 생성 서비스

#### Frontend
- **FileUpload**: 드래그 앤 드롭 파일 업로드
- **ResultsTable**: 결과 테이블 표시
- **ExportButton**: Excel 내보내기 버튼

### 데이터 흐름

1. 사용자가 이미지 업로드
2. Frontend → Backend `/predict` 또는 `/batch`
3. Backend가 예측 수행 (더미)
4. 결과 반환
5. Frontend에 테이블 표시
6. 사용자가 Export 클릭
7. Frontend → Backend `/export/xlsx`
8. Excel 파일 다운로드
