from typing import Container

from aiosales.models import Shop
from aiosales.repositories.abstract import AbstractRepository


class ShopRepository(AbstractRepository[Shop]):
    async def add(self, item: Shop) -> None: ...
    async def get(self, *, reference: int) -> Shop: ...
    async def get_all(self) -> Container[Shop]: ...