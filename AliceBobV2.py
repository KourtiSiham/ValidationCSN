from Str2Tr import Str2Tr
from graph import *
from librarie import *
from SoupModule import *
from Algo import *


class AliceBobConf:
    def __init__(self):
        self.PC_alice = 0
        self.PC_bob = 0

    def __hash__(self):
        return hash(self.PC_alice + self.PC_bob)

    def __eq__(self, other):
        return self.PC_alice == other.PC_alice & self.PC_bob == other.PC_bob

    def __repr__(self):
        return str(self.PC_alice) + str(self.PC_bob)


def InitialtoWaiting_alice(c):
    c.PC_alice = 1


def WaitingtoSC_alice(c):
    return 1


def SCtoInitial_alice(c):
    c.PC_alice = 0


def InitialtoWaiting_bob(c):
    c.PC_bob = 1


def WaitingtoSC_bob(c):
    return 1


def SCtoInitial_bob(c):
    c.PC_bob = 0


def StateCounter():
    soup = SoupProgram(AliceBobConf())

    soup.add(Rule("Alice : Initial to critical section", lambda c: c.PC_alice == 0, InitialtoWaiting_alice))
    soup.add(Rule("Alice : Waiting to critical section", lambda c: c.PC_bob == 0 and c.PC_alice == 1, WaitingtoSC_alice))
    soup.add(Rule("Alice : Critical section to initial state", lambda c: c.PC_alice == 1, SCtoInitial_alice))
    soup.add(Rule("Bob : Initial to waiting state", lambda c: c.PC_bob == 0, InitialtoWaiting_bob))
    soup.add(Rule("Bob : Waiting to critical section", lambda c: c.PC_alice == 0 and c.PC_bob == 1, WaitingtoSC_bob))
    soup.add(Rule("Bob : Critical section to Initial", lambda c: c.PC_bob == 1, SCtoInitial_bob))

    return soup


