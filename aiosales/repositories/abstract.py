import abc
from typing import Generic, TypeVar

T = TypeVar('T')


class AbstractRepository(abc.ABC, Generic[T]):

    @abc.abstractmethod
    def add(self, item):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, *, reference):
        raise NotImplementedError
