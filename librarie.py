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
    
class AcceptingSet:
    def is_accepting(c): pass
class ParentTraceProxy(identifyProxy):
    def __init__(self, operand,dict):
        super().__init__(operand)
        self.dict = dict
    def roots(self):
        neighbours = self.operond.roots()
        for n in neighbours:
            if n not in self.dict:
                self.dict[n] = None
        return neighbours
        #add
    def next(self, source):
        neighbours = self.operand.next(source)
        for n in neighbours:
            if n not in self.dict:
                self.dict[n] = source
        return neighbours


class SemanticTransitionRelation:
    def initialConfigurations (self): pass
    def enablesdActions (self, source): pass
    def execute (self, action, source): pass