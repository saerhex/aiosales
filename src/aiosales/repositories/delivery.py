from aiosales.models import Delivery
from aiosales.repositories.abstract import AbstractRepository


class DeliveryRepository(AbstractRepository[Delivery]):

    async def add(self, item):
        await item.save()

    async def get(self, **reference):
        return await Delivery.filter(**reference).first()

    async def list(self):
        return await Delivery.all()
