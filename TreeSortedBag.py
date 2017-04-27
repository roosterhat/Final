from AbstractBag import AbstractBag

class TreeSortedBag(AbstractBag):
    def __init__(self,item=None,comparator=None):
        self.item = item
        self.left = None
        self.right = None
        self.parent = None
        if comparator is None:
            self.comparator = lambda x,y: x-y
        else:
            self.comparator = comparator

    def __str__(self):
        return str(self.inorder())

    def __len__(self):
        return len(self.inorder())

    def __contains__(self, item):
        return self.inorder().__contains__(item)

    def __iter__(self):
        return self.inorder().__iter__()

    def hasLeft(self):
        return self.left is not None

    def hasRight(self):
        return self.right is not None

    def hasParent(self):
        return self.parent is not None

    def setLeft(self,node):
        if isinstance(node,TreeSortedBag):
            self.left = node

    def setRight(self,node):
        if isinstance(node,TreeSortedBag):
            self.right = node

    def setParent(self,node):
        if isinstance(node,TreeSortedBag):
            self.parent = node

    def unlink(self,node):
        if isinstance(node,TreeSortedBag):
            if self.right == node:
                self.right = None
            elif self.left == node:
                self.left = None

    def add(self,item):
        if self.item is None:
            self.item = item
        else:
            if self.comparator(self.item,item)>=0:
                if self.hasLeft():
                    self.left.add(item)
                else:
                    self.setLeft(TreeSortedBag(item=item))
                    self.left.setParent(self)
            else:
                if self.hasRight():
                    self.right.add(item)
                else:
                    self.setRight(TreeSortedBag(item=item))
                    self.right.setParent(self)

    def delete(self,item):
        if self.comparator(self.item,item)==0:
            if self.hasLeft() or self.hasRight():
                curr = None
                if self.hasRight():
                    curr = self.right
                    while curr.hasLeft():
                        curr = curr.left
                elif self.hasLeft():
                    curr = self.left
                self.item = curr.item
                curr.delete(curr.item)
            else:
                if self.hasParent():
                    self.parent.unlink(self)
                else:
                    self.item = None
        else:
            if self.hasLeft():
                self.left.delete(item)
            if self.hasRight():
                self.right.delete(item)

    def inorder(self):
        res = []
        if self.hasLeft():
            res += self.left.inorder()
        res.append(self.item)
        if self.hasRight():
            res += self.right.inorder()
        return res
