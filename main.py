import inspect
from librarie import *
from hanoi import *
from SoupModule import *
from Str2Tr import Str2Tr
from graph import *
from Algo import *
from AliceBobV1 import *
from AliceBobV2 import *
from AliceBobV3 import *
from nbits import *


def Hanoi_Main():
    num_of_disks = 3
    num_of_stacks = 3
    hanoi_tower = identifyProxy(Hanoi(num_of_disks, num_of_stacks))
    init = hanoi_tower.initial()[0]
    print("Before Soup")
    for i, j in [(0, 2), (0, 1), (2, 1), (0, 2), (1, 0), (1, 2), (0, 2)]:
        guard = guarde_def(i, j)
        action = action_def(i, j)
        g = guard(init)
        if g:
            a = action(init)
        print(f'{i},{j} : {"True" if g else "False"} -> {init}')

    print("-------------------------")
    print("Soup")
    soup = hanoi_soap(3, 3)
    Behavior_Soup = SoupSemantics(soup)
    init = Behavior_Soup.initialConfigurations()[0]
    print("First State: ", init)
    actions = Behavior_Soup.enabledActions(init)

    if actions:
        for action in actions:
            execute = Behavior_Soup.execute(init, action)
            print("Output : ", execute)

    str = Str2Tr(Behavior_Soup)
    init = str.roots()[0]
    next = str.next(init)
    print("After ", init, ": ", next)


def AliceBobV1_Main():
    semantic = SoupSemantics(StateCounter())
    r = predicate_model_checker(semantic, lambda c: c.PC_alice == 1 and c.PC_bob == 0)
    print(r)
    r = predicate_model_checker(semantic, lambda c: len(semantic.enabledActions(c)) == 0)
    print(r)


def AliceBobV2_Main():
    semantic = SoupSemantics(StateCounter())
    tr = Str2Tr(semantic)
    tr = IsAcceptingProxy(tr, lambda c: c.PC_alice == 0)
    print(tr.roots())
    print(tr.next(tr.roots()[0]))
    r = predicate_model_checker(semantic, lambda c: c.PC_alice == 0 and c.PC_bob == 1)
    print(r)
    # r = predicate_model_checker(semantic, lambda c: len(semantic.enabledActions(c)) == 0)
    # print(r)


def AliceBobV3_Main():
    semantic = SoupSemantics(AliceAndBob())
    r = predicate_model_checker(semantic, lambda c: c.PC_alice == 2 and c.PC_bob == 2)
    print(r)  # False <-- since they cannot be at the same time in the critical section
    r = predicate_model_checker(semantic, lambda c: len(semantic.enabledActions(c)) == 0)
    print(r)


def Nbits_Main():
    x = 16
    [predicate, target, found, count], known = predicate_finder(NBits([0], 3), lambda n: n == x)
    print(f'{x} reachable: ', found, ' explored ', count, 'nodes, known: ', binary_print(known))

    x = 5
    [predicate, target, found, count], known = predicate_finder(NBits([0], 3), lambda n: n == x)
    print(f'{x} reachable: ', found, ' explored ', count, 'nodes, known: ', binary_print(known))

    x = 1
    [predicate, target, found, count], known = predicate_finder(NBits([0], 3), lambda n: n == x)
    print(f'{x} reachable: ', found, ' explored ', count, 'nodes, known: ', binary_print(known))


if __name__ == "__main__":
    while True:
        Choice = input('\n*****************************************************************\n'
                       'Choose an option from the following list: \n'
                       '1. Run Nbits \n'
                       '2. Run Hanoi to get the two solutions (With and without soup) \n'
                       '3. Run V1 of Alice and Bob\n'
                       '4. Run V2 of Alice and Bob\n'
                       '5. Run V3 of Alice and Bob\n')

        if Choice == '1':
            Nbits_Main()
        elif Choice == '2':
            Hanoi_Main()
        elif Choice == '3':
            AliceBobV1_Main()
        elif Choice == '4':
            AliceBobV2_Main()
        elif Choice == '5':
            AliceBobV3_Main()
        else:
            print("Please choose an option from the list")
