from typing import Container

from aiosales.models import Order
from aiosales.repositories.abstract import AbstractRepository


class OrderRepository(AbstractRepository[Order]):
    async def add(self, item: Order) -> None: ...
    async def get(self, *, reference: int) -> Order: ...
    async def get_all(self) -> Container[Order]: ...