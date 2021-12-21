from typing import List, Optional

from dependency_injector.wiring import inject
from dependency_injector.wiring import Provide
from fastapi import APIRouter
from fastapi import Depends
from fastapi import Query
from fastapi import status
from starlette.responses import FileResponse, StreamingResponse, Response
from starlette.templating import Jinja2Templates

from aiosales.containers import Container
from aiosales.containers import Dispatcher
from aiosales.pydantic_models import OrderPostPydantic
from aiosales.services.orders import OrdersService
from aiosales.services.products import ProductsService
from aiosales.utils import extract_values_from_dict, generate_pdf

router = APIRouter(
    prefix='/ishops',
    tags=['ishops'],
)

templates = Jinja2Templates(directory="templates")


@router.post('/orders', status_code=status.HTTP_201_CREATED)
@inject
async def create_order(
    order: OrderPostPydantic,
    orders_service: OrdersService = Depends(Provide[Container.orders_service])
):
    order_data = order.dict()
    shop_id, product_id = extract_values_from_dict(
        order_data,
        keys=['shop_id', 'product_id']
    )
    await orders_service.create_order(order_data, shop_id, product_id)


@router.get('/orders')
@inject
async def list_orders(
    shops: Optional[List[str]] = Query(...),
    products: Optional[List[str]] = Query(...),
    orders_service: OrdersService = Depends(Provide[Container.orders_service]),
    dispatcher: Dispatcher = Depends(Provide[Container.pydantic_models_dispatcher])
):
    orders = await orders_service.filter_orders(shops=shops, products=products)
    serialized = await dispatcher.models['orders_list'].from_queryset(orders)
    return serialized


@router.get('/products/metrics')
@inject
async def get_shop_metrics(
    products_service: ProductsService = Depends(Provide[Container.products_service])
):
    products_with_metrics = await products_service.get_with_metrics()
    template = templates.get_template('report.html')
    html = template.render(products=products_with_metrics)
    file = generate_pdf(html=html)
    return Response(file, media_type='application/pdf')
