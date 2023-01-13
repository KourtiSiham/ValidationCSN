
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
