from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends, status

from aiosales.containers import Container
from aiosales.pydantic_models import OrderPydantic
from aiosales.services.orders import OrdersService

router = APIRouter()


@router.post('/orders', status_code=status.HTTP_201_CREATED)
@inject
async def create_order(
        order: OrderPydantic,
        orders_service: OrdersService = Depends(Provide[Container.orders_service])
):
    await orders_service.create_order(order_data=order.dict())


@router.get('/orders')
async def _():
    ...


@router.get('/{shop_id}/metrics')
async def _():
    ...
