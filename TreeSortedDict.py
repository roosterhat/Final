from AbstractDictionary import AbstractDictionary

class TreeSortedDict(AbstractDictionary):
    def __init__(self,key=None,value=None,comparator=lambda x,y:x-y,parent=None):
        self.key = key
        self.value = value
        self._left = None
        self._right = None
        self._parent = parent
        self.comparator = comparator

    def __len__(self):
        res = 1
        if self.hasLeft():
            res += len(self.getLeft())
        if self.hasRight():
            res += len(self.getRight())
        return res

    def __del__(self):
        del self[self.key]

    def __delitem__(self, key):
        self.delete(key)

    def __setitem__(self, key, value):
        self.insert(key,value)

    def __iter__(self):
        return self.inorder().__iter__()

    def __getitem__(self, key):
        return self.get(key)

    def __str__(self):
        return "(<key: "+str(self.key)+" item: "+str(self.value)+">"+str(self.getLeft())+str(self.getRight())+")"

    def __contains__(self, value):
        if self.comparator(value,self.value)==0:
            return True
        if self.comparator(value,self.value)<0:
            if self.hasLeft():
                if self.getLeft(). __contains__(value):
                    return True
        else:
            if self.hasRight():
                if self.getRight(). __contains__(value):
                    return True
        return False

    def hasValue(self):
        return self.value is not None

    def hasLeft(self):
        return self._left is not None

    def hasRight(self):
        return self._right is not None

    def hasParent(self):
        return self._parent is not None

    def getLeft(self):
        return self._left

    def getRight(self):
        return self._right

    def setLeft(self,node):
        if isinstance(node,TreeSortedDict) or node is None:
            self._left = node

    def setRight(self,node):
        if isinstance(node,TreeSortedDict) or node is None:
            self._right = node

    def getParent(self):
        return self._parent

    def setParent(self,node):
        if isinstance(node,TreeSortedDict) or node is None:
            self._parent = node

    def findKey(self,value):
        if self.value==value:
            return self.key
        if self.hasLeft():
            res = self.getLeft().findKey(value)
            if res is not None:
                return res
        if self.hasRight():
            res = self.getRight().findKey(value)
            if res is not None:
                return res

    def unlink(self,node):
        if self.getLeft() == node:
            self.setLeft(None)
        if self.getRight() == node:
            self.setRight(None)

    def pop(self):
        val = self
        self.delete(self.key)
        return val

    def insert(self, key, item):
        if not self.hasValue():
            self.value = item
            self.key = key
        else:
            if self.comparator(key,self.key)>0:
                if self.hasRight():
                    self.getRight().insert(key,item)
                else:
                    self.setRight(TreeSortedDict(key=key,value=item,comparator=self.comparator,parent=self))
            else:
                if self.hasLeft():
                    self.getLeft().insert(key,item)
                else:
                    self.setLeft(TreeSortedDict(key=key,value=item,comparator=self.comparator,parent=self))


    def delete(self,key):
        if self.comparator(key,self.key)==0:
            if self.hasRight():
                curr = self.getRight()
                while curr.hasLeft():
                    curr = curr.left
                self.value = curr.value
                self.key = curr.key
                curr.delete(curr.key)
            elif self.hasLeft():
                curr = self.getLeft()
                while curr.hasRight():
                    curr = curr.right
                self.value = curr.value
                self.key = curr.key
                curr.delete(curr.key)
            else:
                if self.hasParent():
                    self.getParent().unlink(self)
        else:
            if self.comparator(key,self.key)<0:
                if self.hasLeft():
                    self.getLeft().delete(key)
            else:
                if self.hasRight():
                    self.getRight().delete(key)

    def inorder(self):
        res = []
        if self.hasLeft():
            res += self.getLeft().inorder()
        res.append("<key: "+str(self.key)+" item: "+str(self.value)+">")
        if self.hasRight():
            res += self.getRight().inorder()
        return res

    def get(self, key):
        if self.comparator(key,self.key)==0:
            return self.value
        if self.comparator(key,self.key)<0:
            if self.hasLeft():
                return self.getLeft().get(key)
        else:
            if self.hasRight():
                return self.getRight().get(key)



"""
bt = TreeSortedDict()
bt.insert(5,"test5")
bt.insert(3,"test3")
bt.insert(6,"test6")
bt.insert(7,"test7")
bt.insert(4,"test4")
bt.insert(1,"test1")
bt.insert(2,"test2")
bt[8] = "test8"

print(bt)

del bt[8]

print(bt)

print(bt.findKey("test6"))
print(bt[bt.findKey("test6")])
print(bt.findKey("test61"))
print(bt.inorder())
print()

del bt[5]

print(bt)
print(bt.inorder())
print()"""