from AbstractDictionary import AbstractDictionary

class LinkedDict(AbstractDictionary):
    def __init__(self,key=None,value=None):
        self.key = key
        self.value = value
        self._child = None
        self._parent = None

    def __len__(self):
        res = 1
        if self.hasChild():
            res += len(self.getChild())
        return res

    def __delitem__(self, key):
        self.delete(key)

    def __setitem__(self, key, value):
        self.insert(key,value)

    def __iter__(self):
        return self.toList().__iter__()

    def __getitem__(self, key):
        return self.get(self.index(key))

    def __str__(self):
        res = "{key: "+str(self.key)+", item: "+str(self.value)+"}"
        if self.hasChild():
            res += ","+str(self.getChild())
        return res

    def __contains__(self, key):
        if self.key == key:
            return self.value
        elif self.hasChild():
            return key in self.getChild()
        else:
            return False

    def hasValue(self):
        return self.value is not None

    def hasChild(self):
        return self._child is not None

    def hasParent(self):
        return self._parent is not None

    def getChild(self):
        return self._child

    def setChild(self,node):
        if isinstance(node,LinkedDict) or node is None:
            self._child = node

    def getParent(self):
        return self._parent

    def setParent(self,node):
        if isinstance(node,LinkedDict) or node is None:
            self._parent = node

    def pop(self):
        val = self.value
        self.delete(self.key)
        return val

    def insert(self, key, item):
        if not self.hasValue():
            self.value = item
            self.key = key
        else:
            if self.hasChild():
                self.getChild().insert(key,item)
            else:
                self.setChild(LinkedDict(key=key,value=item))
                self.getChild().setParent(self)

    def index(self, key,index=0):
        if self.key==key:
            return index
        else:
            if self.hasChild():
                return self.getChild().index(key,index=index+1)
            else:
                return -1

    def delete(self, key):
        if self.key==key:
            if self.hasParent():
                if self.hasChild():
                    self.getParent().setChild(self.getChild())
                else:
                    self.getParent().setChild(None)
            else:
                if self.hasChild():
                    self.value = self.getChild().value
                    self.key = self.getChild().key
                    self.setChild(self.getChild().getChild())
                else:
                    self.value = None
                    self.key = None
                    self.setChild(None)
        elif self.hasChild():
            self.getChild().delete(key)


    def get(self, index=0):
        if index==0:
            return self.value
        elif self.hasChild():
            return self.getChild().get(index=(index-1))

    def remove(self, key):
        self.delete(key)

    def toList(self):
        string = ["{key: "+str(self.key)+", item: "+str(self.value)+"}"]
        if self.hasChild():
            return string + self.getChild().toList()
        return string

import random
a = LinkedDict()
for i in range(10):
    a[random.randint(0,10000)] = "test"

a[1234] = "this is a test"

print(a)
print(len(a))
print(a[1234])
#print(1234 in a)
del a[1234]
print(a)
print(len(a))
print(a.toList())



