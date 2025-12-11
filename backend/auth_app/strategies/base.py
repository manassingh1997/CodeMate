from abc import ABC, abstractmethod

# Base class for authentication strategies
class AuthStrategy(ABC):
    @abstractmethod
    def authenticate(self, request):
        pass