from tortoise.queryset import QuerySet

from aiosales.models import Product
from aiosales.repositories.product import ProductRepository

class ProductsService:
    product_repo: ProductRepository
    def __init__(self, product_repo: ProductRepository) -> None: ...
    async def get_by_id(self, _id: int) -> Product: ...
    async def get_with_metrics(self) -> QuerySet[Product]: ...