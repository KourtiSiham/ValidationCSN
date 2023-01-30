from Str2Tr import Str2Tr
from graph import *
from librarie import *
from SoupModule import *


class AliceBobConfiguration:
    def __init__(self):
        self.PC_alice = 0
        self.PC_bob = 0
        self.Flag_alice = 0
        self.Flag_bob = 0

    def __hash__(self):
        return hash(self.PC_alice + self.PC_bob) + hash(self.Flag_alice + self.Flag_bob)

    def __eq__(self, other):
        if other is None:
            return False
        return self.PC_alice == other.PC_alice and self.PC_bob == other.PC_bob and self.Flag_bob == other.Flag_bob and self.Flag_alice == other.Flag_alice

    def __repr__(self):
        return str(self.PC_alice) + str(self.PC_bob)


def AliceBob():
    soup = SoupProgram(AliceBobConfiguration())

    def ItoW_alice(c):
        c.PC_alice = 1
        c.Flag_alice = 1

    soup.add(Rule("ItoSC_alice", lambda c: c.PC_alice == 0, ItoW_alice))

    def WtoSC_alice(c):
        c.PC_alice = 2
        c.Flag_alice = 1

    soup.add(Rule("WtoSC_alice", lambda c: c.PC_bob != 2 and c.PC_alice == 1, WtoSC_alice))

    def SCtoI_alice(c):
        c.PC_alice = 0
        c.Flag_alice = 0

    soup.add(Rule("SCtoI_alice", lambda c: c.PC_alice == 2, SCtoI_alice))

    def ItoW_bob(c):
        c.PC_bob = 1
        c.Flag_bob = 1

    soup.add(Rule("ItoW_bob", lambda c: c.PC_bob == 0, ItoW_bob))

    def WtoSC_bob(c):
        c.PC_bob = 2
        c.Flag_bob = 1

    soup.add(Rule("WtoSC_bob", lambda c: c.PC_bob == 1 and c.PC_alice != 2, WtoSC_bob))

    def SCtoI_bob(c):
        c.PC_bob = 0
        c.Flag_bob = 0

    soup.add(Rule("SCtoI_bob", lambda c: c.PC_bob == 2, SCtoI_bob))

    return soup


def a_in_cs(c):
    return c.PC_alice == 2


def b_in_cs(c):
    return c.PC_bob == 2


if __name__ == '__main__':
    semantic = SoupSemantics(AliceBob())
    # r = predicate_model_checker(semantic, lambda c: c.PC_alice == 2 and c.PC_bob == 2)
    # print(r)
    # r = predicate_model_checker(semantic, lambda c: len(semantic.actions(c)) == 0)
    # print(r)
