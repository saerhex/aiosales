from aiosales.models import Delivery
from aiosales.repositories.abstract import AbstractRepository


class DeliveryRepository(AbstractRepository[Delivery]):

    async def add(self, item):
        await item.save()

    async def get(self, *, reference):
        return await Delivery.filter(id=reference).first()

    async def get_all(self):
        return await Delivery.all()
