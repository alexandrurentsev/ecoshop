from fastapi import APIRouter, UploadFile
import shutil

router = APIRouter(
    prefix="/images",
    tags=["Загрузка картинок"]
)


@router.post("/products")
async def add_product_image(id_images: int, file: UploadFile):
    with open(f"static/images/{id_images}.webp", "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
