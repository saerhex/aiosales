from typing import Dict, List, Union

from tortoise.queryset import QuerySet

from aiosales.models import Order
from aiosales.repositories.order import OrderRepository
from aiosales.repositories.product import ProductRepository
from aiosales.repositories.shop import ShopRepository

class OrdersService:
    shop_repo: ShopRepository
    product_repo: ProductRepository
    order_repo: OrderRepository
    def __init__(
        self,
        shop_repo: ShopRepository,
        product_repo: ProductRepository,
        order_repo: OrderRepository
    ) -> None: ...
    async def create_order(self, order_data: Dict[str, Union[int, str]], shop_id: int, product_id: int) -> None: ...
    async def filter_orders(self, shops: List[str], products: List[str], **attributes: Union[str, int]) -> QuerySet[Order]: ...
