from AbstractBag import AbstractBag

class LinkedBag(AbstractBag):
    def __init__(self,value=None):
        self.item = value
        self.child = None
        self.parent = None
        self._iterator = LBagIter(self)

    def __len__(self):
        length = 1
        if self.hasChild():
            length += len(self.child)
        return length

    def __contains__(self, item):
        if self.item==item:
            return True
        else:
            if self.hasChild():
                return self.child.__contains__(item)
            else:
                return False

    def __str__(self):
        res = str(self.item)
        if self.hasChild():
            res += ","+str(self.child)
        return res

    def __iter__(self):
        return self._iterator

    def hasChild(self):
        return self.child is not None

    def hasParent(self):
        return self.parent is not None

    def hasItem(self):
        return self.item is not None

    def setChild(self,child):
        if isinstance(child,LinkedBag):
            self.child = child

    def setParent(self,parent):
        if isinstance(parent,LinkedBag):
            self.parent = parent

    def unlink(self):
        self.setChild(None)

    def add(self,item):
        if not self.hasItem():
            self.item = item
        elif self.hasChild():
            self.child.add(item)
        else:
            self.setChild(LinkedBag(value=item))
            self.child.setParent(self)

    def delete(self,item):
        if self.item==item:
            if self.hasChild():
                if self.hasParent():
                    self.parent.setChild(self.child)
                else:
                    self.item = self.child.item
                    self.child = None
            else:
                if self.hasParent():
                    self.parent.unlink()
                else:
                    self.item = None
        elif self.hasChild():
            self.child.delete(item)

    def getAmount(self,item):
        count = 0
        if self.item==item:
            count += 1
        if self.hasChild():
            count += self.child.getAmount(item)
        return count

class LBagIter:
    def __init__(self,start=None):
        if isinstance(start,LinkedBag):
            self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is not None:
            value = self.current
            if self.current.hasChild():
                self.current = self.current.child
            else:
                self.current = None
            return value
        else:
            raise StopIteration()

