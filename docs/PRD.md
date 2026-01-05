# Product Requirements Document (PRD)
## RiceVarietyVision MVP

### 개요
RiceVarietyVision은 쌀 품종 이미지를 분석하여 품종을 자동으로 분류하는 AI 기반 웹 애플리케이션입니다.

### 목표
- 쌀 이미지를 업로드하여 품종을 자동 분류
- 배치 처리 지원
- 결과를 Excel로 내보내기
- 신뢰도(confidence) 기반 시각화

### 주요 기능 (Phase 1-2)

#### 1. 이미지 업로드
- 단일 이미지 업로드
- 드래그 앤 드롭 지원
- 배치 업로드 (여러 이미지)

#### 2. 품종 분류
- 이미지 분석 및 품종 예측
- 신뢰도 점수 제공
- 3개 품종 라벨: "백미", "현미", "흑미" (초기 더미)

#### 3. 결과 표시
- 테이블 형태로 결과 표시
- 신뢰도 기반 색상 코딩
- 정렬 및 필터링

#### 4. Excel 내보내기
- 결과를 Excel 파일로 다운로드
- 신뢰도 기반 조건부 서식 적용

### 기술 스택
- Backend: FastAPI
- Frontend: React/Next.js
- Excel: openpyxl
- 이미지 처리: PIL/Pillow
