class Node(object):

    def __init__(self, value=None, left=None, right=None, parent=None):
        self.left = left
        self.right = right
        self.parent = parent
        self.value = value

    def get_parent(self):
        return self.parent

    def set_parent(self, new):
        if type(new) is Node or new is None:
            self.parent = new
        else:
            print("Not of valid type!")

    def get_right(self):
        return self.right

    def set_right(self, new):
        if type(new) is Node or new is None:
            self.right = new
        else:
            print("Not of valid type!")

    def get_left(self):
        return self.left

    def set_left(self, new):
        if type(new) is Node or new is None:
            self.left = new
        else:
            print("Not a valid type")

    def get_value(self):
        return self.value

    def set_value(self, val):
        self.value = val

class BinarySearchTree(object):

    def __init__(self, root=None):
        self.root = root

    # is_empty: void -> boolean
    # Returns true if list is empty false otherwise
    def is_empty(self):
        return self.root == None

    # insert: Node -> void
    # Inserts new into sorted BST
    def insert(self, item):
        new = Node(value=item)

        if self.root is None:
            self.root = new
        else:
            self._insert_helper(self.root, None, new, "")

    def dfs(self, root):
        path = []
        if root is None:
            return path
        else:
            path += root.get_value()
        path += self.dfs(root.get_left())
        path += self.dfs(root.get_right())

    def __iter__(self):
        return self.dfs(self.root).__iter__()

    def __str__(self):
        for i in self:
            print(i)

    # _insert_helper: Node, Node, Node, String -> Void
    # Take Current Node, Previous Node, New Node, and Last Direction
    def _insert_helper(self, node, prev, new, dir):
        if node is None:
            if dir == "R":
                prev.set_right(new)
            elif dir == "L":
                prev.set_left(new)
            new.set_parent(prev)

        elif new.get_value() < node.get_value():
            self._insert_helper(node.get_left(), node, new, "L")
        else:
            self._insert_helper(node.get_right(), node, new, "R")

    # delete: int -> Void
    # Deletes value in the BST
    def delete(self, value):
        if not self.in_order_find(value):
            print("Not in tree, cannot delete!")
        else:
            self._delete_helper(value, self.root)

    # (private)_find_min(): Node -> Node
    # Finds the minimum of a subtree by going left repeatedly
    def _find_min(self, node):
        if node.get_left() is None:
            return node
        self._find_min(node.get_left())

    # (private)_replace_node: Node, Node -> Void
    # Takes new node and current node, and swaps.
    def _replace_node(self, value, node):
        if node.get_parent() is not None:
            if node is node.get_parent().get_left():
                node.get_parent().set_left(value)
            else:
                node.get_parent().set_right(value)
        if value is not None:
            value.set_parent(node.get_parent())

    # (private)_delete_helper: int, Node -> Void
    # Finds number and deletes by 3 cases:
    # 1. Node has no children - Remove Node
    # 2. Node has one child - Remove Node, replace with child
    # 3. Node has two children - Find min, replace value, swap if need be and remove
    def _delete_helper(self, value, node):
        # If value is neither < nor >, then it is correct value.
        if value < node.get_value():
            self._delete_helper(value, node.get_left())
        elif value > node.get_value():
            self._delete_helper(value, node.get_right())
        else:
            # Case 2 children
            # Put min value in node, run from min node. Min can have child, must be right-side
            if node.get_right() is not None and node.get_left() is not None:
                next = self._find_min(node.get_right())
                node.set_value(next.get_value())
                self._delete_helper(next.get_value(), next)
            # Case left child only
            elif node.get_left() is not None:
                self._replace_node(node.get_left(), node)
            # Case right child only
            elif node.get_right() is not None:
                self._replace_node(node.get_right(), node)
            # Case no children
            else:
                self._replace_node(None, node)

    # Searching algorithms: Pre-order, In-Order, Post-Order
    def find(self, value):
        return self.pre_order_find(value) and self.post_order_find(value) and self.in_order_find(value)

    # pre_order_find: int -> boolean
    # Returns true if 'value' is in BST, else false
    def pre_order_find(self, value):
        return self._pre_order_find_helper(self.root, value)

    # (private)_pre_order_find_helper: Node, int -> boolean
    # Uses pre-order BST algorithm to determine if value exists
    def _pre_order_find_helper(self, root, value):
        if root is None:
            return False
        print(root.get_value())
        if value == root.get_value():
            return True
        if self._pre_order_find_helper(root.get_left(), value):
            return True
        if self._pre_order_find_helper(root.get_right(), value):
            return True
        return False

    # in_order_find: int -> boolean
    # Returns true if 'value' is in BST, else false
    def in_order_find(self, value):
        return self._in_order_find_helper(self.root, value)

    # (private)_in_order_find_helper: Node, int -> boolean
    # Uses in-order BST algorithm to determine if value exists
    def _in_order_find_helper(self, root, value):
        if root is None:
            return False
        if self._in_order_find_helper(root.get_left(), value):
            return True
        if value == root.get_value():
            return True
        if self._in_order_find_helper(root.get_right(), value):
            return True
        return False

    # post_order_find: int -> boolean
    # Returns true if 'value' is in BST, else false
    def post_order_find(self, value):
        return self._post_order_find_helper(self.root, value)

    # (private)_post_order_find_helper: Node, int -> boolean
    # Uses post-order BST algorithm to determine if value exists
    def _post_order_find_helper(self, root, value):
        if root is None:
            return False
        if self._post_order_find_helper(root.get_left(), value):
            return True
        if self._post_order_find_helper(root.get_right(), value):
            return True
        if value == root.get_value():
            return True
        return False
