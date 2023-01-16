from librarie import *


class Str2Tr(TransitionRelation):
    def __init__(self, astr):
        self.astr = astr

    def roots(self):
        return self.astr.initialConfigurations()

    def next(self, s):
        targets = []
        for a in self.astr.enablesdActions(s):
            target = self.astr.execute(a, s)
            targets.append(target)
        return targets
