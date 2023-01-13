from TransitionRelation import TransitionRelation

class Hanoi(TransitionRelation):
    def __init__(self, n, rods):
        self.n = n
        self.rods = rods
    def roots(self):
        return (list(range(1, self.n+1)), 0, self.n-1, *self.rods)

    def next(self, source):
        src_peg = source[1]
        dst_peg = source[2]
        top_of_src = self.rods[src_peg].pop()
        if rods[dst_peg]:
            top_of_dst = self.rods[dst_peg][-1]
        else:
            top_of_dst = None
        if not top_of_dst or top_of_src < top_of_dst:
            self.rods[dst_peg].append(top_of_src)
            return (source[0], src_peg, dst_peg, *self.rods)
        else:
            self.rods[src_peg].append(top_of_src)
            return None
if __name__ == "__main__":
    n = 3
    rods = [list(range(n, 0, -1)), [], []]
    h = Hanoi(n, rods)
    initial_state = h.roots()
    print("Initial state: ", initial_state)
    state = initial_state
    while state:
        print("Next state: ", state)
        state = h.next(state)