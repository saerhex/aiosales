from typing import Any

from tortoise.queryset import QuerySet

from aiosales.models import Shop
from aiosales.repositories.abstract import AbstractRepository

class ShopRepository(AbstractRepository[Shop]):
    async def add(self, item: Shop) -> None: ...
    async def get(self, **reference: Any) -> Shop: ...
    async def list(self) -> QuerySet[Shop]: ...