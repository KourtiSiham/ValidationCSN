from TransitionRelation import TransitionRelation
import itertools

class Nbits(TransitionRelation):
    def __init__(self, n):
        self.n = n

    def roots(self):
        return list(itertools.product([0, 1], repeat=self.n))

    def next(self, source):
        next_state = []
        carry = 1
        for i in range(self.n):
            val = (source[i] + carry) % 2
            next_state.append(val)
            carry = (source[i] + carry) // 2
        return tuple(next_state)

if __name__ == "__main__":
    n = 2
    nb = Nbits(n)
    initial_state = nb.roots()
    print("Initial states: ", initial_state)
    for state in initial_state:
        print("Next states for ", state)
        for i in range(len(initial_state)):
            next_state = nb.next(state)
            print(next_state)
            state = next_state
