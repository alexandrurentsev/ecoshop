from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from rest_v1.product.views import get_all_products

router = APIRouter(prefix="/pages", tags=["Фронтенд"])

templates = Jinja2Templates(directory="templates")


@router.get("/products")
# в любом endpoint, который принимает jinja - добавлять request
async def get_products_page(request: Request, products=Depends(get_all_products)):
    name = "products.html"

    return templates.TemplateResponse( 
        name=name, context={"request": request, "products": products}
    )
