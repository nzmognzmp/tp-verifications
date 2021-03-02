from collections import defaultdict


class RuleSet:
    def __init__(self):
        self.deps = defaultdict(set)
        self.conflicts = defaultdict(set)

    def add_dep(self, a, b):
        self.deps[a].add(b)

    def add_conflict(self, a, b):
        self.conflicts[a].add(b)
        self.conflicts[b].add(a)

    def is_coherent(self):
        options = frozenset(self.deps)
        for option in options:
            deps = self.compute_deps(option)
            for dep in deps:
                if self.conflicts[dep] & deps:
                    return False
        return True

    def compute_deps(self, option):
        to_visit = {option}
        deps = set()
        while to_visit:
            dep = to_visit.pop()
            deps.add(dep)
            to_visit.update(self.deps.get(dep, set()) - deps)
        return deps
