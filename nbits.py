from librarie import TransitionRelation
from Algo import predicate_finder

class NBits(TransitionRelation):

    def __init__(self, roots: list, n: int):
        self.initial = roots
        self.nBits = n

    def roots(self):
        return self.initial

    def next(self, source):
        neighbours = []
        for i in range(self.nBits):
            neighbours.append(source ^ (1 << i))
        return neighbours


def binary_print(s):
    return set(map(
        lambda x: "{0:03b}".format(x),
        s))
