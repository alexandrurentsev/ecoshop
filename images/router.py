from fastapi import APIRouter, UploadFile
import shutil

from tasks.tasks import process_pic

router = APIRouter(
    prefix="/images",
    tags=["Загрузка картинок"]
)


@router.post("/products")
async def add_product_image(id_images: int, file: UploadFile):
    image_path = f"static/images/{id_images}.webp"
    with open(image_path, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
    process_pic.delay(image_path)
