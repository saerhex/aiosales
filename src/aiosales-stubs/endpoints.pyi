from typing import List, Optional

from fastapi import APIRouter
from starlette.responses import Response
from starlette.templating import Jinja2Templates
from tortoise.contrib.pydantic import PydanticListModel

from aiosales.containers import Dispatcher
from aiosales.pydantic_models import OrderPostPydantic, ProductPostPydantic, ShopPostPydantic
from aiosales.services.orders import OrdersService
from aiosales.services.products import ProductsService
from aiosales.services.shops import ShopService

router = APIRouter

templates = Jinja2Templates


async def create_order(
        order: OrderPostPydantic,
        orders_service: OrdersService
) -> None: ...


async def list_orders(
        shops: Optional[List[str]],
        products: Optional[List[str]],
        orders_service: OrdersService,
        dispatcher: Dispatcher
) -> PydanticListModel: ...


async def get_shop_metrics(
        products_service: ProductsService
) -> Response: ...


async def create_product(
        product: ProductPostPydantic,
        products_service: ProductsService
) -> None: ...


async def create_shop(
        shop: ShopPostPydantic,
        shop_service: ShopService
) -> None: ...
