from aiosales.models import Shop
from aiosales.repositories.abstract import AbstractRepository


class ShopRepository(AbstractRepository[Shop]):

    async def add(self, item):
        await item.save()

    async def get(self, *, reference):
        return await Shop.filter(id=reference).first()

    async def get_all(self):
        return await Shop.all()
