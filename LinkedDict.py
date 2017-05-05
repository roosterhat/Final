from AbstractDictionary import AbstractDictionary
from AbstractDictionary import Entry
from linked_structure import LinkedStructure


class LinkedDict(AbstractDictionary, LinkedStructure):
    def __init__(self, key=None, value=None,comp=lambda x, y: x == y.key):
        if key is not None:
            LinkedStructure.__init__(self, Entry(key, value), comp=comp)
        else:
            LinkedStructure.__init__(self, comp=comp)

    def __getitem__(self, key):
        return LinkedStructure.__getitem__(self, self.index(key))

    def add(self, entry):
        if isinstance(entry, Entry):
            LinkedStructure.add(self, entry)

    def insert(self, index, entry):
        if isinstance(entry, Entry):
            LinkedStructure.insert(index, entry)


import random

a = LinkedDict()
for i in range(10):
    a[random.randint(0, 10000)] = "test"

a[1234] = "this is a test"

print(a)
print(len(a))
print(a[1234])
# print(1234 in a)
del a[1234]
print(a)
print(len(a))
print(a.toList())
