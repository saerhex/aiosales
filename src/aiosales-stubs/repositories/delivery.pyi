from typing import Any

from tortoise.queryset import QuerySet

from aiosales.models import Delivery
from aiosales.repositories.abstract import AbstractRepository

class DeliveryRepository(AbstractRepository[Delivery]):
    async def add(self, item: Delivery) -> None: ...
    async def get(self, **reference: Any) -> Delivery: ...
    async def list(self) -> QuerySet[Delivery]: ...