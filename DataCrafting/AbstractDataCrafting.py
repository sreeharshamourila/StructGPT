from abc import ABC, abstractmethod

class DataCrafting(ABC):
    @abstractmethod
    def craft_for_database(self, data):
        pass

    @abstractmethod
    def craft_for_frontend(self, data):
        pass

