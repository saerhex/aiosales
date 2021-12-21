from fastapi.routing import APIRouter

from aiosales.services.orders import OrdersService
from src.aiosales.pydantic_models import OrderPydantic

router: APIRouter


async def create_order(order: OrderPydantic, order_service: OrdersService) -> None: ...