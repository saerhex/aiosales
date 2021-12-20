from typing import Container

from aiosales.models import Delivery
from aiosales.repositories.abstract import AbstractRepository


class DeliveryRepository(AbstractRepository[Delivery]):
    async def add(self, item: Delivery) -> None: ...
    async def get(self, *, reference: int) -> Delivery: ...
    async def get_all(self) -> Container[Delivery]: ...