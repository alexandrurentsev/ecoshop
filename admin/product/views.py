
from sqladmin import ModelView
from product.models import Product


class ProductAdmin(ModelView, model=Product):
    column_list = [c.name for c in Product.__table__.c]
    name = "Продукт"
    name_plural = "Продукты"
    icon = "fa fa-lemon"
