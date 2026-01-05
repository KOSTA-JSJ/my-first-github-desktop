from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import health, predict, export

app = FastAPI(
    title="RiceVarietyVision API",
    description="쌀 품종 이미지 분류 API",
    version="1.0.0"
)

# CORS 설정 (프론트엔드와 통신을 위해)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000", "http://localhost:5174"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 라우터 등록
app.include_router(health.router, tags=["Health"])
app.include_router(predict.router, tags=["Prediction"])
app.include_router(export.router, tags=["Export"])


@app.get("/")
async def root():
    return {
        "message": "RiceVarietyVision API",
        "version": "1.0.0",
        "docs": "/docs"
    }
