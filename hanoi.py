import copy
import sys
from librarie import TransitionRelation

class Hanoi(TransitionRelation):
    def __init__(self, nb_stacks, nb_disks):
        super().__init__()
        self.nbDisks = nb_disks
        self.nbStacks = nb_stacks

    def initial(self):
        return [HanoiConfiguration(self.nbStacks, self.nbDisks)]

    def next(self, n):
        next_states = []
        for i in range(self.nbStacks):
            new_node = copy.deepcopy(n)
            if new_node[i]:
                disk = new_node[i].pop()
                for j in range(self.nbStacks):
                    if i != j and (not new_node[j] or new_node[j][-1] > disk):
                        temp = copy.deepcopy(new_node)
                        temp[j].append(disk)
                        next_states.append(temp)
        return next_states
    
    def roots(self):
        return self.initial()
  
class HanoiConfiguration(list):
    def __init__(self, nb_stacks, nb_disks):
        list.__init__(self, [[(nb_disks - i) for i in range(nb_disks)]] + [[] for _ in range(nb_stacks - 1)])

    def __hash__(self):
        hash = 0
        maxi = max(self)[0]
        for stack in self:
            hash += sum(stack) * maxi
            maxi *= 2
        return hash

    def __eq__(self, conf):
        if len(self) != len(conf):
            return False
        for i in range(len(self)):
            if len(self[i]) != len(conf[i]):
                return False
        for j in range(len(self)):
            if conf[j] != self[j]:
                return False
        return True
if __name__ == "__main__":
    hanoi = Hanoi(7, 6)
    initial_config = hanoi.initial()[0]
    print("Initial Configuration: ", initial_config)
    current_config = initial_config
    while True:
        next_configs = hanoi.next(current_config)
        if not next_configs:
            break
        current_config = next_configs[0]
        print("Next Configuration: ", current_config)
        k = 0
        if not current_config[-1]:
            continue
        for disk in current_config[-1]:
            if disk != hanoi.nbDisks - k:
                continue
            k = k + 1
        print("Solution found!")
        break
