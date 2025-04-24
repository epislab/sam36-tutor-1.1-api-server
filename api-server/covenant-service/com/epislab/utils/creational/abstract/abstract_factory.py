from abc import ABC, abstractmethod

# ✅ 1. 올바른 추상 클래스 정의 (Abstract Factory)
class AbstractFactory(ABC):
    @abstractmethod
    def create(self, *args, **kwargs):
        """팩토리 메서드 - 서브클래스에서 반드시 구현해야 함"""
        pass