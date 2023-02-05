from abc import ABC, abstractmethod


class TransitionRelation(ABC):
    @abstractmethod
    def roots(self):
        pass

    @abstractmethod
    def next(self, source):
        pass


class identifyProxy(object):
    def __init__(self, operand):
        self.operand = operand

    def __getattr__(self, attr):
        return getattr(self.operand, attr)


class ReplaceRootsProxy(identifyProxy):
    def __init__(self, operand, newRoots):
        super().__init__(operand)
        self.newRoots = newRoots  # new configurations

    def roots(self):
        return self.newRoots


class AcceptingSet:
    def is_accepting(c):
        pass


class ParentTraceProxy(identifyProxy):
    def __init__(self, operand, dict=None):
        super().__init__(operand)
        if dict == None:
            dict = {}
        self.dict = dict

    def roots(self):
        neighbours = self.operand.roots()
        for n in neighbours:
            if n not in self.dict:
                self.dict[n] = None
        return neighbours
        # add

    def next(self, source):
        neighbours = self.operand.next(source)
        for n in neighbours:
            if n not in self.dict:
                self.dict[n] = [source]
        return neighbours

    def get_trace(dic, target):
        result = []
        current = target
        while current in dic:
            result.append(current)
            current = dic[current]
        return result[::-1]


class IsAcceptingProxy(identifyProxy):
    def __init__(self, operand, predicate):
        super().__init__(operand)
        self.predicate = predicate

    def isAccepting(self, c):
        return self.predicate(c)


class SemanticTransitionRelation:
    def initialConfigurations(self):
        pass

    def enablesdActions(self, source):
        pass

    def execute(self, action, source):
        pass


class InputSemanticTransitionRelation:
    def initial(self):
        pass

    def enablesdActions(self, input, source):
        pass

    def execute(self, action, input, source):
        pass
