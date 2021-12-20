from typing import Container

from aiosales.models import Product
from aiosales.repositories.abstract import AbstractRepository



class ProductRepository(AbstractRepository[Product]):
    async def add(self, item: Product) -> None: ...
    async def get(self, *, reference: int) -> Product: ...
    async def get_all(self) -> Container[Product]: ...