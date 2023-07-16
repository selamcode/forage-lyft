from abc import ABC, abstractmethod

# Serviceable interface
class Serviceable(ABC):

    @abstractmethod
    def needs_service(self):
        pass