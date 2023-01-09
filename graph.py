

from abc import abstractmethod


class TransactionRelation:
     @abstractmethod
     def roots(self): pass

     @abstractmethod
     def next(self,source): pass
     

#class du graphe
"""class Graph :
    def __init__(self,g):
        self.dict = g
        self.initial_value = g[next(iter(g))]

    def initial_index(self):
        return next(iter(self.dict))

    def graph(self):
        return self.dict

    def initial(self):
        return self.initial_value

    def next(self,m):
        return self.dict[m]
"""""""""""