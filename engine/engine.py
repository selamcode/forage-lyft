from abc import ABC, abstractmethod


# engine interface
class Engine(ABC):
    
    @abstractmethod
    def needs_service(self):
        pass