from aiosales.models import Product
from aiosales.repositories.abstract import AbstractRepository


class ProductRepository(AbstractRepository[Product]):

    async def add(self, item):
        await item.save()

    async def get(self, *, reference):
        return await Product.filter(id=reference).first()

    async def get_all(self):
        return await Product.all()
