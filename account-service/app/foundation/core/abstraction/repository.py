from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')

class BaseRepository(ABC, Generic[T]):
    @abstractmethod
    async def save(self, entity: T) -> T:
        pass

    @abstractmethod
    async def get(self, id: str) -> T:
        pass 