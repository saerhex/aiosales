from aiosales.models import Order
from aiosales.repositories.abstract import AbstractRepository


class OrderRepository(AbstractRepository[Order]):

    async def add(self, item):
        await item.save()

    async def get(self, **reference):
        return await Order.filter(**reference).first()

    async def list(self):
        return await Order.all()

    async def filter(self, filter_set):
        return Order.filter(filter_set)
