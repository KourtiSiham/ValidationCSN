from Str2Tr import Str2Tr
from graph import *
from librarie import *
from SoupModule import *
from Algo import *


class AliceBobConf:
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


def InitialtoWaiting_alice(c):
    c.PC_alice = 1
    c.Flag_alice = 1


def WaitingtoSC_alice(c):
    c.PC_alice = 2
    c.Flag_alice = 1


def SCtoInitial_alice(c):
    c.PC_alice = 0
    c.Flag_alice = 0


def InitialtoWaiting_bob(c):
    c.PC_bob = 1
    c.Flag_bob = 1


def WaitingtoSC_bob(c):
    c.PC_bob = 2
    c.Flag_bob = 1


def SCtoInitial_bob(c):
    c.PC_bob = 0
    c.Flag_bob = 0


def AliceIsInCS(c):
    return c.PC_alice == 2


def BobIsInSC(c):
    return c.PC_bob == 2


def AliceAndBob():
    soup = SoupProgram(AliceBobConf())

    soup.add(Rule("Alice : Initial state to critical section", lambda c: c.PC_alice == 0, InitialtoWaiting_alice))
    soup.add(Rule("Alice : Waiting state to critical section", lambda c: c.PC_bob != 2 and c.PC_alice == 1, WaitingtoSC_alice))
    soup.add(Rule("Alice : Critical section to Initial state", lambda c: c.PC_alice == 2, SCtoInitial_alice))
    soup.add(Rule("Bob : Initial state to Waiting state", lambda c: c.PC_bob == 0, InitialtoWaiting_bob))
    soup.add(Rule("Bob : Waiting state to critical section", lambda c: c.PC_bob == 1 and c.PC_alice != 2, WaitingtoSC_bob))
    soup.add(Rule("Bob : Critical section to Initial state", lambda c: c.PC_bob == 2, SCtoInitial_bob))

    return soup
