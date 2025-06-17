from abc import ABC, abstractmethod

class FileHandler(ABC):

    def __init__(self, factory_entry):
        self._factory_entry = factory_entry

    
    @abstractmethod
    def read_card(file_name):
        pass

    @abstractmethod
    def write_file(cards):
        pass

    