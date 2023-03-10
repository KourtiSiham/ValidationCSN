
from collections import deque


graph1 = dict () 
graph1['a'] = ['b','d']
graph1['b']= ['e','c']
graph1['c']=['a']
graph1['d']=['d','e']
graph1['e']=['f']
graph1['f']=[]


class Graph :
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

graphO = Graph(graph1)

def bfs(g,i) :
    known = set()
    frontier = deque()
    at_start = True
    while frontier or at_start :
        source = None
        if at_start :
            neighbours = g.initial()
            at_start = False
            known.add(g.initial_index())
        else :
            source = frontier.popleft()
            neighbours = g.next(source)
        for n in neighbours :
            if n in known :
                continue
            known.add(n)
            frontier.append(n)
    return known

def bfs_target(g,target) :
    known = set()
    frontier = deque()
    at_start = True
    while frontier or at_start :
        source = None
        if at_start :
            neighbours = g.initial()
            at_start = False
            if target == g.initial_index() :
                return True
            known.add(g.initial_index())
        else :
            source = frontier.popleft()
            neighbours = g.next(source)
        for n in neighbours :
            if n == target :
                return True
            if n in known :
                continue
            known.add(n)
            frontier.append(n)
    return False

# def on_entry(s,n,o) :
#     return
#
# def on_known(s,n,o) :
#     return
#
# def on_exit(s,n,o) :
#     return

def bfs_v2(g,acc,f1,f2,f3) :
    known = set()
    frontier = deque()
    at_start = True
    while frontier or at_start:
        source = None
        if at_start:
            neighbours = g.initial()
            at_start = False
            if acc == g.initial_index():
                return True
            known.add(g.initial_index())
        else:
            f1()
            source = frontier.popleft()
            neighbours = g.next(source)
        for n in neighbours:
            if n == acc:
                return True
            if n in known:
                f2()
                continue
            f3()
            known.add(n)
            frontier.append(n)
    return False


print(bfs(graphO,'a'))

print(bfs_target(graphO,'a'))