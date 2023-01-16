from librarie import *
from librarie import SemanticTransitionRelation

class Str2Tr(TransitionRelation):
    def __init__(self, astr):
        self.astr = astr

    # def roots(self):
    #     return astr.initialConfigurations()

    def initial(self):
        return self.operand.initial()

    def next(self, s):
        targets = []
        for a in self.operand.actions(s):
            target = self.operand.execute(s, a)
            targets.append(target)
        return targets
