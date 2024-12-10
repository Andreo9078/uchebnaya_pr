from abc import ABC, abstractmethod

class BaseRole(ABC):

    @abstractmethod
    def create_interface(self):
        pass

    @abstractmethod
    def clear_window(self):
        pass