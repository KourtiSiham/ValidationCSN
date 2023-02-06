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


def InitialtoSC_alice(c):
    c.PC_alice = 1


def SCtoInitial_alice(c):
    c.PC_alice = 0


def InitialtoSC_bob(c):
    c.PC_bob = 1


def SCtoInitial_bob(c):
    c.PC_bob = 0


def StateCounter():
    soup = SoupProgram(AliceBobConf())
    #  If alice is still at the initial state (at home) then Counter will be 1 and access to critical section
    soup.add(Rule("Alice : Initial to critical section", lambda c: c.PC_alice == 0, InitialtoSC_alice))
    #  If alice is still at the critical section (garden) then Counter will be 0 and return home
    soup.add(Rule("Alice : Critical section to Initial state", lambda c: c.PC_alice == 1, SCtoInitial_alice))
    soup.add(Rule("Alice : Initial state to critical section", lambda c: c.PC_bob == 0, InitialtoSC_alice))
    soup.add(Rule("Bob: Critical section to Initial state", lambda c: c.PC_bob == 1, SCtoInitial_bob))

    return soup