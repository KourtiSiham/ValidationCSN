import inspect
from collections import deque
from librarie import *
from Str2Tr import *


def bfs(graph, acc, on_entry=lambda source, n, acc: False, on_known=lambda source, n, acc: False,
        on_exit=lambda source, acc: False):
    known = set()
    frontier = deque()
    at_start = True
    while frontier or at_start:
        source = None
        if at_start:
            neighbours = graph.roots()
            at_start = False
        else:
            source = frontier.popleft()
            neighbours = graph.next(source)
        for n in neighbours:
            if n in known:
                if on_known(source, n, acc):
                    return acc, known
                continue
            known.add(n)
            frontier.append(n)
            if on_entry(source, n, acc):
                return acc, known
        if on_exit(source, acc):
            return acc, known
    return acc, known


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


def iterative_bfs(graph):
    visited = []
    queue = deque()
    init = True
    while len(queue) != 0 | init:
        if init:
            voisin = graph.roots()
            init = False
        else:
            node = queue.popleft()
            voisin = graph.next(node)
        for n in voisin:
            if n not in visited:
                if graph.isAccepting(n):
                    return True
                queue.append(n)
                visited.append(n)
    return False


def predicate_finder(
        graph,
        predicate=lambda n: False):
    def check_predicate(s, n, a):
        # increment the count
        a[2] += 1
        # check predicate
        a[1] = predicate(n)
        # set the node that checks the predicate in the last field of the accumulator
        if a[1]:
            a[3] = n
        # return true if predicate is true - stop the traversal
        return a[1]

    return bfs(graph, [predicate, False, 0, None], on_entry=check_predicate)


def predicate_model_checker(semantic, predicate):
    tr = Str2Tr(semantic)
    tr = IsAcceptingProxy(tr, predicate)
    predicate_mc(tr, predicate)
    return iterative_bfs(tr)


def get_trace(parents, n, i):
    trace = [n]
    try:
        parent = parents[n]
    except KeyError:
        parent = None
    if isinstance(parent, list):
        parent = parent[0] if len(parent) > 0 else None
    while parent is not None:
        trace.append(parent)
        if parent in i:
            return trace
        try:
            parent = parents[parent]
            if isinstance(parent, list):
                parent = parent[0] if len(parent) > 0 else None
        except KeyError:
            parent = None
    return trace


def predicate_mc(transition_relation, predicate):
    print(f'{"-" * 50}\npredicate model-checking for:\n{inspect.getsource(predicate)}')

    op_tracer = ParentTraceProxy(transition_relation)

    [pred, found, count, target], known = predicate_finder(op_tracer, predicate)
    print(f'has reachable accepting state {found} after exploring ', count, ' configurations')

    the_trace = []
    if found is True:
        the_trace = get_trace(op_tracer.dict, target, op_tracer.roots())
        trace_string = f'\n{"-" * 20}\n'.join(str(x) for x in the_trace)
        print(f'The trace is: \n{trace_string}')