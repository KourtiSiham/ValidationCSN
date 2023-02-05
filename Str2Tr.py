from librarie import *


class Str2Tr(TransitionRelation):
    def __init__(self, astr):
        self.astr = astr

    def roots(self):
        return self.astr.initialConfigurations()

    def next(self, s):
        targets = []
        for a in self.astr.enabledActions(s):
            target = self.astr.execute(s, a)
            targets.append(target)
        return targets
