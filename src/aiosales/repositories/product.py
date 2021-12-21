from tortoise.query_utils import Prefetch

from aiosales.models import Order
from aiosales.models import Product
from aiosales.repositories.abstract import AbstractRepository


class ProductRepository(AbstractRepository[Product]):

    async def add(self, item):
        await item.save()

    async def get(self, **reference):
        return await Product.filter(**reference).first()

    async def list(self):
        return await Product.all()

    async def filter_with_done_delivery(self):
        return await Product \
            .all() \
            .prefetch_related(
                Prefetch(
                    'orders',
                    queryset=Order.filter(
                        delivery__status="DONE"
                    )
                ),
                'orders__shop'
            )
