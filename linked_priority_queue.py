from Collection.abstract_priority_queue import AbstractPriorityQueue
from Collection.abstract_priority_queue import PriorityNode
from Collection.abstract_collection import AbstractCollection
from Collection.linked_structure import LinkedStructure


class LinkedPriorityQueue(AbstractPriorityQueue):

    def __init__(self, other=None):
        self._items = LinkedStructure()
        if other:
            for item in other:
                self.add(item)
        AbstractCollection.__init__(self)


if __name__ == "__main__":
    pqueue = LinkedPriorityQueue()
    pn = PriorityNode(5, 5)
    pqueue.push(pn)
    pn = PriorityNode(0, 1)
    pqueue.push(pn)
    pn = PriorityNode(3, 3)
    pqueue.push(pn)
    print(pqueue)
    print(pqueue.peek())
    pqueue.pop()
    print(pqueue)