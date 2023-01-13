from abc import ABC, abstractmethod

class TransitionRelation(ABC):
    @abstractmethod
    def roots(self):
        pass

    @abstractmethod
    def next(self, source):
        pass
