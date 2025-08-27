from fastapi import APIRouter
import fastapi
from fastapi.responses import FileResponse

import os

documents = APIRouter(
        prefix="/documents",
        tags=["Documents"]
    )

@documents.get("/oferta")
async def get_oferta_pdf():
    file_path = "./documents/oferta.pdf"
    if not os.path.exists(file_path):
        raise fastapi.HTTPException(status_code=404, detail="Oferta PDF not found")
    return FileResponse(file_path, media_type="application/pdf")


@documents.get("/politika_konf")
async def get_oferta_pdf():
    file_path = "./documents/politika_konf.pdf"
    if not os.path.exists(file_path):
        raise fastapi.HTTPException(status_code=404, detail="Politika_konf PDF not found")
    return FileResponse(file_path, media_type="application/pdf")


@documents.get("/skan_ip")
async def get_oferta_pdf():
    file_path = "./documents/skan_IP.pdf"
    if not os.path.exists(file_path):
        raise fastapi.HTTPException(status_code=404, detail="Skan_IP PDF not found")
    return FileResponse(file_path, media_type="application/pdf")