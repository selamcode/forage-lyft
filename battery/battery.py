from abc import ABC, abstractmethod 

# battery interface
class Battery(ABC):
   
    @abstractmethod # not required but good practice
    def needs_service(self):
        pass
