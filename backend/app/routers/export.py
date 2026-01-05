from fastapi import APIRouter
from fastapi.responses import StreamingResponse, JSONResponse
from app.models import ExportRequest
from app.services.exporter import export_to_excel

router = APIRouter()


@router.post("/export/xlsx")
async def export_xlsx(request: ExportRequest):
    """Excel 파일로 내보내기"""
    try:
        # Excel 파일 생성
        excel_file = export_to_excel(request.results)
        
        # 파일명 생성
        filename = f"rice_variety_results.xlsx"
        
        # 스트리밍 응답 반환
        return StreamingResponse(
            excel_file,
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            headers={"Content-Disposition": f"attachment; filename={filename}"}
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"Excel 내보내기 중 오류 발생: {str(e)}"}
        )
