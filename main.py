from librarie import *
from hanoi import *


def main_hanoi_1():
    # Input: number of disks
    num_of_disks = 4

    # Create three stacks of size 'num_of_disks'
    # to hold the disks
    src = createStack(num_of_disks)
    dest = createStack(num_of_disks)
    aux = createStack(num_of_disks)

    tohIterative(num_of_disks, src, aux, dest)

def main_hanoi_2():
    print("-------------------------")
    print("Guarde / Action")
    print("Example 1: ")
    hanoi_tower = ParentTraceProxy(Hanoi(3,3))
    for i, j in [(0, 1), (0, 2), (2, 1)]:
        init = hanoi_tower.initial()[0]
        guarde = guarde_def(i, j)
        action = action_def(i, j)
        g = guarde(init)
        if g:
            a = action(init)
        print(f'{i},{j} : {"Vrai" if g else "Faux"} -> {init}')

    print("Example 2: ")
    init = hanoi_tower.initial()[0]
    for i, j in [(0, 2), (0, 1), (2, 1), (0, 2), (1, 0), (1, 2), (0, 2)]:
        guard = guarde_def(i, j)
        action = action_def(i, j)
        g = guard(init)
        if g:
            a = action(init)
        print(f'{i},{j} : {"Vrai" if g else "Faux"} -> {init}')

    print("-------------------------")
    print("Soup")
    soup = hanoi_soap(3, 3)
    Behavior_Soup = SoupSemantics(soup)
    init = Behavior_Soup.initial()[0]
    print("First State: ", init)
    actions = Behavior_Soup.actions(init)

    if actions:
        print("Possible action : ", inspect.getsource(action))
        for action in actions:
            execute = Behavior_Soup.execute(init, action)
            print("Execution output : ", execute)

    print("-------------------------")

    print("STR2TR")
    str = Str2Tr(Behavior_Soup)
    init = str.initial()[0]
    next = str.next(init)
    print("States after ", init, "are", next)

    print("-------------------------")

    print("Kripke Buchi")
if __name__ == "__main__":
    main_hanoi_1()
