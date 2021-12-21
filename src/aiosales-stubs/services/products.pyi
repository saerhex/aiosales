from datetime import timedelta
from decimal import Decimal
from typing import Dict, Union

from tortoise.queryset import QuerySet

from aiosales.models import Product
from aiosales.repositories.product import ProductRepository
from aiosales.repositories.shop import ShopRepository


class ProductsService:
    product_repo: ProductRepository
    shop_repo: ShopRepository
    def __init__(self, product_repo: ProductRepository, shop_repo: ShopRepository) -> None: ...
    async def get_by_id(self, _id: int) -> Product: ...
    async def get_with_metrics(self) -> QuerySet[Product]: ...
    async def create_product(
        self,
        product_data: Dict[str, Union[str, Decimal, int, timedelta, Dict]],
        shop_id: int
    ) -> None: ...
