from Collection.abstract_heap import abstract_heap
from Collection.array import Array

class ArrayHeap(abstract_heap):

    def __init__(self):
        self._items = Array(100)
        abstract_heap.__init__(self)

