from fastapi import APIRouter, Body
from fastapi.responses import StreamingResponse
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

router = APIRouter()

@router.post("/generate-memo", response_class=StreamingResponse)
async def generate_pdf(memo_text: str = Body(..., embed=True)):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    
    # Very simple PDF generation
    text_object = p.beginText(40, 800)
    text_object.setFont("Helvetica", 12)

    for line in memo_text.split('\n'):
        text_object.textLine(line)
    
    p.drawText(text_object)
    p.showPage()
    p.save()

    buffer.seek(0)
    return StreamingResponse(buffer, media_type='application/pdf', headers={
        "Content-Disposition": "inline; filename=memo.pdf"
    })
