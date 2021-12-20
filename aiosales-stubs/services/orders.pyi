from typing import Union, Dict

from repositories.order import OrderRepository
from repositories.product import ProductRepository
from repositories.shop import ShopRepository


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
    async def create_order(
        self,
        order_data: Dict[str, Union[int, str]]
    ) -> None: ...