from dependency_injector import providers
from dependency_injector import containers

from aiosales.repositories.product import ProductRepository
from aiosales.repositories.shop import ShopRepository
from aiosales.repositories.order import OrderRepository
from aiosales.services.orders import OrdersService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration(yaml_files=['configs/config.yml'])

    wiring_config = containers.WiringConfiguration(
        modules=[
            '.endpoints'
        ]
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


