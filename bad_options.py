from ruleset import RuleSet
import pprint

class Options:


    def __init__(self, rule_set):
        self.rule_set = rule_set
        self.selected = set()


    def selection(self):
        """Selection"""
        return self.selected


    def remove_dependents(self, options):
        to_remove = set(options)
        done = False
        while not done:
            done = True
            for i, other_option in enumerate(self.selected):
                    if to_remove & self.rule_set.compute_deps(other_option):
                        if other_option not in to_remove:
                            done = False
                        to_remove.add(other_option)
        self.selected -= to_remove


    def toggle(self, option):
        """
        Toggle an option.

        :param option: Which option to toggle.
        :param verbose: Print which options were selected or unselected.
        """
        if option in self.selected:
            self.remove_dependents(option)
        else:
            deps = self.rule_set.compute_deps(option)
            self.remove_dependents(
                set().union(*[self.rule_set.conflicts[d] for d in deps])
            )
            self.selected |= deps
