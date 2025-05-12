from abc import ABCMeta, abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession

class AbstractService(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, db: AsyncSession, **kwargs): pass