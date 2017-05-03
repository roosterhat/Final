from Collection.abstract_collection import AbstractCollection


class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __str__(self):
        return str(self.data)


class LinkedStructure(AbstractCollection):
    def __init__(self, other=None):
        self._head = None
        self._tail = None
        AbstractCollection.__init__(self, other)

    def __iter__(self):
        temp = self._head
        while temp is not None:
            yield temp
            temp = temp.next

    def __str__(self):
        out = "["
        counter = 0
        for item in self:
            if counter != 0:
                out += ","
            out += str(item.data)
            counter += 1
        out += "]"
        return out

    def add(self, item):
        if self._head is None:
            self._head = Node(item, None, None)
            self._tail = self._head
        else:
            temp = Node(item, self._tail, None)
            self._tail.next = temp
            self._tail = temp
        self._size += 1

    def insert(self, index, value):
        if self._size == 0:
            self.add(value)
        elif index == 0:
            temp = Node(value, None, self._head)
            self._head.prev = temp
            self._head = temp
            self._size += 1
        else:
            if index >= self._size:
                self.add(value)
            else:
                for item in self:
                    if index == 1:
                        break
                    index -= 1
                temp = Node(value, item, item.next)
                item.next.prev = temp
                item.next = temp
                self._size += 1

    def __getitem__(self, index):
        if index >= self._size or index < 0:
            raise IndexError("Index out of bounds")
        else:
            return self._getNode(index).data

    def _getNode(self, index):
        for item in self:
            if index == 0:
                return item
            index -=1

    def __setitem__(self, index, value):
        self._getNode(index).data = value

    def remove(self, index):
        if index >= self._size or index < 0:
            raise IndexError("Index :" + index + " is out of bound")
        else:
            if index == 0:
                newHead = self._head.next
                if newHead is not None:
                    newHead.prev = None
                self._head.next = None
                self._head = newHead
            elif index == self._size - 1:
                newTail = self._tail.prev
                self._tail.prev = None
                self._tail = newTail
                self._tail.next = None
            else:
                node = self._getNode(index)
                node.prev.next = node.next
                node.next.prev = node.prev
                node.prev = None
                node.next = None
            self._size -= 1

    def clear(self):
        self._head = None
        self._tail = self._head
        self._size = 0


if __name__ == "__main__":
    lyst = LinkedStructure([1, 2, 3, 4])
    print(lyst.__str__())
    lyst.insert(5, 100)
    print(lyst)
    lyst.remove(2)
    print(lyst)
