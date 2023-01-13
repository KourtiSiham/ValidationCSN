def bfs(graph):
    known = set()  # Known
    frontier = []  # Frontier #list_des_noeuds
    at_start = True  # init

    while frontier or at_start:
        if at_start:
            neighbours = graph.initial()
            at_start = False
        else:
            neighbours = graph.next(frontier.popleft())
        for n in neighbours:

            if n not in known:
                known.add(n)
                frontier.append(n)

    return known

