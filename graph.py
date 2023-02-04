from collections import deque
from queue import Queue
from Algo import bfs_iterative,predicate_finder,bfs
from librarie import TransitionRelation

class GraphData(TransitionRelation):
    def __init__(self,ini,graph):
        self.initial = ini
        self.graph = graph
    def roots(self):
        return self.initial

    def next(self, a):
        try:
          return self.graph[a]
        except KeyError:
            return []

def main_BFS():
    g = {
        0: [1, 3],
        1: [2],
        2: [0],
        3: [3, 4],
        4: [1, 5],
        5: [],
        6: []
        }

    graph1 = GraphData([1], g)

    def e1(s, n, a):
        # increment the count
        a[2] += 1
        # is the current node equal to the target ?
        a[1] = a[0] == n
        # return true if target found
        return a[1]

    [target, found, count], known = bfs(graph1, [3, False, 0], on_entry=e1)
    print(found, ' explored ', count, 'nodes, known: ', known)

    [target, found, count], known = bfs(graph1, [5, False, 0], on_entry=e1)
    print(found, ' explored ', count, 'nodes, known: ', known)

    [target, found, count], known = bfs(graph1, [1, False, 0], on_entry=e1)
    print(found, ' explored ', count, 'nodes, known: ', known)

    [target, found, count], known = bfs(graph1, [0, False, 0], on_entry=e1)
    print(found, ' explored ', count, 'nodes, known: ', known)

    [target, found, count], known = bfs(graph1, [6, False, 0], on_entry=e1)
    print(found, ' explored ', count, 'nodes, known: ', known)

    graph1 = GraphData([0, 6], g)
    print('-------------------------')

    [target, found, count], known = bfs(graph1, [3, False, 0], on_entry=e1)
    print(found, ' explored ', count, 'nodes, known: ', known)

    [target, found, count], known = bfs(graph1, [5, False, 0], on_entry=e1)
    print(found, ' explored ', count, 'nodes, known: ', known)

    [target, found, count], known = bfs(graph1, [1, False, 0], on_entry=e1)
    print(found, ' explored ', count, 'nodes, known: ', known)

    [target, found, count], known = bfs(graph1, [0, False, 0], on_entry=e1)
    print(found, ' explored ', count, 'nodes, known: ', known)

    [target, found, count], known = bfs(graph1, [6, False, 0], on_entry=e1)
    print(found, ' explored ', count, 'nodes, known: ', known)

    [target, found, count], known = bfs(graph1, [10, False, 0], on_entry=e1)
    print(found, ' explored ', count, 'nodes, known: ', known)

    print('-----------------PREDICATE FINDER--------')
    [pred, found, count, target], known = predicate_finder(graph1, lambda n: n == 3)
    print('pred(', target, ')=', found, ' explored ', count, 'nodes, known: ', known)

    [pred, found, count, target], known = predicate_finder(graph1, lambda n: n == 5)
    print('pred(', target, ')=', found, ' explored ', count, 'nodes, known: ', known)

    [pred, found, count, target], known = predicate_finder(graph1, lambda n: n == 1)
    print('pred(', target, ')=', found, ' explored ', count, 'nodes, known: ', known)

    [pred, found, count, target], known = predicate_finder(graph1, lambda n: n == 0)
    print('pred(', target, ')=', found, ' explored ', count, 'nodes, known: ', known)

    [pred, found, count, target], known = predicate_finder(graph1, lambda n: n == 6)
    print('pred(', target, ')=', found, ' explored ', count, 'nodes, known: ', known)

    [pred, found, count, target], known = predicate_finder(graph1, lambda n: n == 10)
    print('pred(', target, ')=', found, ' explored ', count, 'nodes, known: ', known)
if __name__ == '__main__':
    main_BFS()
  
   