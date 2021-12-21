from dataclasses import dataclass
from typing import Dict, Union

from dependency_injector import containers
from dependency_injector import providers
from fastapi import FastAPI
from tortoise.contrib.pydantic import PydanticListModel
from tortoise.contrib.pydantic import PydanticModel

from aiosales.repositories.order import OrderRepository
from aiosales.repositories.product import ProductRepository
from aiosales.repositories.shop import ShopRepository
from aiosales.services.orders import OrdersService
from aiosales.services.products import ProductsService
from aiosales.services.shops import ShopService


@dataclass
class Dispatcher:
    models: Dict[str, Union[PydanticListModel, PydanticModel]]


class Container(containers.DeclarativeContainer):
    config: providers.Configuration

    wiring_config: containers.WiringConfiguration

    app: FastAPI

    database: providers.Resource

    pydantic_models_dispatcher: Dispatcher

    shop_repo: ShopRepository
    product_repo: ProductRepository
    order_repo: OrderRepository

    orders_service: OrdersService
    products_service: ProductsService
    shop_service: ShopService
