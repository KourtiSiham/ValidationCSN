from librarie import *
import copy


class Rule:
    def __init__(self, name, guard, action):
        self.name = name
        self.guard = guard
        self.action = action

    def execute(self, config):
        return [self.action(config)]


class SoupProgram:
    def __init__(self, ini):
        self.ini = ini
        self.rules = []

    def add(self, rule):
        self.rules.append(rule)


class SoupSemantics(SemanticTransitionRelation):
    def __init__(self, program):
        self.program = program

    def initialConfigurations(self):
        return [self.program.ini]

    def enabledActions(self, source):
        return filter(lambda r: r.guard(source), self.program.rules)  # To be checked

    def execute(self, action, source):
        target = source.copy  # copy.deepcopy(source)
        return action.execute(target)

class InputSoupSemantics(InputSemanticTransitionRelation):
    def __init__(self, program):
        self.program = program

    def initial(self):
        return [self.program.init]

    def enabledActions(self, input, source):
        return filter(lambda r: r.guard(input, source), self.program.rules)

    def execute(self, action, input, source):
        target = copy.deepcopy(source)
        n = action(input, target)
        return [target]


