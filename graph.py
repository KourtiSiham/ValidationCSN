from collections import deque
from queue import Queue

class Node:
    def _init_(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def _str_(self):
        return "Node %s" % self.value

    def _repr_(self):
        return self._str_()



def bfs_iterative(starting_node, visited=[]):
    queue = []
    queue.insert(0, starting_node)
    visited.append(starting_node)
    while len(queue) != 0:
        current_node = queue.pop()
        # print(current_node.value)
        for child in current_node.children:
            if child not in visited:
                queue.insert(0, child)
                visited.append(child)
    return visited


class GraphData:
    def _init_(self):
        self.initial = None
        self.graph = {}

    def add(self, a, neighbours, initial=False):
        self.graph[a] = neighbours
        if initial:
            assert self.initial == None
            self.initial = self.graph[a]

    def get_neighbours(self, a):
        return self.graph[a]

    def get_initial(self):
        return self.initial



def bfs(data, on_discovery=lambda source, n: None, on_known=lambda source, n: None):
    knowns = set()
    queue = Queue()
    queue.put(data.get_initial())
    knowns.add(data.get_initial())
    while not queue.empty():
        source = queue.get()
        neighbours = data.get_neighbours(source)
        for n in neighbours:
            if n in knowns:
                on_known(source, n)
                continue
            on_discovery(source, n)
            queue.put👎
            knowns.add👎
    return knowns

if _name_ == "_main_":
    data = GraphData()
    parent = "a"
    children = ["b", "c", "d"]
    children_b = ["e", "f"]
    children_c = ["r", "t"]

    data.add("a", children, initial=True)
    data.add("b", children_b)
    data.add("c", children_c)
    data.add("d", [])
    data.add("e", [])
    data.add("f", ["f"])
    data.add("r", [])
    data.add("t", ["a"])

    # Create nodes
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")
    r = Node("r")
    t = Node("t")

    # Add children to nodes
    a.add_child(b)
    a.add_child(c)
    a.add_child(d)
    b.add_child(e)
    b.add_child(f)
    c.add_child(r)
    c.add_child(t)

    # Perform a breadth-first traversal starting from node "a"
    print("\n Breadth-first traversal:")
    visited_nodes = bfs_iterative(a)
    print(visited_nodes)

    """
       # The graph will look like this
       #
       #       a
       #    / / \ \
       #   b    c  d
       #  / \    /\
       # e   f  r   t
       #       |
       #       a
       """