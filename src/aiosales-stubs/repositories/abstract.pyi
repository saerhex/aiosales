import abc
from typing import Any, Generic, TypeVar

T = TypeVar('T')

class AbstractRepository(abc.ABC, Generic[T]):
    @abc.abstractmethod
    async def add(self, item: T) -> None: ...
    @abc.abstractmethod
    async def get(self, **reference: Any) -> T: ...
