import abc
from typing import Generic, TypeVar, Any

T = TypeVar('T')

class AbstractRepository(abc.ABC, Generic[T]):
    @abc.abstractmethod
    async def add(self, item: T) -> None: ...
    @abc.abstractmethod
    async def get(self, *, reference: Any) -> T: ...
