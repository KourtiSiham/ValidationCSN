from abc import ABC, abstractmethod

class TransitionRelation(ABC):
    @abstractmethod
    def roots(self):
        pass

    @abstractmethod
    def next(self, source):
        pass



class identifyProxy:
    def __init__(self, operand):
        self.operand = operand

    def __getattr__(self, attr):
        return getattr(self.operand, attr)


class ReplaceRootsProxy(identifyProxy):
    def __init__(self, operand ,newRoots):
        super().__init__(operand)

class ParentStoreProxy(identifyProxy):
    def __init__(self, operand):
        super().__init__(operand)
        self.parent = {}

    def next(self, conf):
        ns = self.operand.next(conf)

        for n in ns:
            if n not in self.parent:
                self.parent[n] = conf, None
        return ns