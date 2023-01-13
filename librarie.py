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
        self.newRoots = newRoots
    def roots(self):
        return self.newroots    
    

class ParentTraceProxy(identifyProxy):
    def __init__(self, operand,dict):
        super().__init__(operand)
        self.dict = dict
    def roots(self):
        neighbours = self.operond.roots()
        #add
    def next(self, source):
        neighbours = self.operand.next(source)
        for n in neighbours:
            if n not in self.dict:
                self.dict[n] = source, None
        return neighbours

     