from abc import ABC, abstractmethod

class AbstractLlms(ABC):

    @abstractmethod
    def chat(context:str) -> str:
        pass