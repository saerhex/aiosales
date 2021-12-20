from aiosales.models import Order
from aiosales.repositories.abstract import AbstractRepository


class OrderRepository(AbstractRepository[Order]):

    async def add(self, item):
        await item.save()

    async def get(self, *, reference):
        return await Order.filter(id=reference).first()

    async def get_all(self):
        return await Order.all()
