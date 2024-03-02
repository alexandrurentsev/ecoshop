from tasks.celery import celery
from PIL import Image
from pathlib import Path


@celery.task
def process_pic(
    path: str
):
    image_path = Path(path)
    image = Image.open(image_path)
    image_resized_1000_500 = image.resize((1000, 500))
    image_resized_200_100 = image.resize((200, 100))
    # TODO вынести пути в переменные/настройки
    image_resized_1000_500.save(f"static/images/resized_1000_500_{image_path.name}")
    image_resized_200_100.save(f"static/images/resized_200_100_{image_path.name}")
