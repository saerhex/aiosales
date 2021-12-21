from dataclasses import dataclass
from typing import Dict, Union

from dependency_injector import containers
from dependency_injector import providers
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from tortoise.contrib.pydantic import pydantic_queryset_creator
from tortoise.contrib.pydantic import PydanticListModel
from tortoise.contrib.pydantic import PydanticModel

from aiosales.models import Order
from aiosales.repositories.order import OrderRepository
from aiosales.repositories.product import ProductRepository
from aiosales.repositories.shop import ShopRepository
from aiosales.services.orders import OrdersService
from aiosales.services.products import ProductsService


@dataclass
class Dispatcher:
    models: Dict[str, Union[PydanticListModel, PydanticModel]]


class Container(containers.DeclarativeContainer):
    config = providers.Configuration(yaml_files=['configs/config.yml'])

    wiring_config = containers.WiringConfiguration(
        modules=[
            '.endpoints'
        ]
    )

    app = providers.Singleton(FastAPI)

    database = providers.Resource(
        register_tortoise,
        app=app,
        db_url=config.database.url,
        generate_schemas=True,
        modules={
            'models': [
                'aiosales.models'
            ]
        }
    )

    pydantic_models_dispatcher = providers.Factory(
        Dispatcher,
        models=providers.Dict(
            orders_list=providers.Factory(pydantic_queryset_creator, cls=Order),
        )
    )

    shop_repo = providers.Singleton(ShopRepository)
    product_repo = providers.Singleton(ProductRepository)
    order_repo = providers.Singleton(OrderRepository)

    orders_service = providers.Factory(
        OrdersService,
        shop_repo=shop_repo,
        product_repo=product_repo,
        order_repo=order_repo,
    )

    products_service = providers.Factory(
        ProductsService,
        product_repo=product_repo
    )
