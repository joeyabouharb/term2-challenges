deleted = False
class BST:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.size = 0
        
    def insert(self, value):
        self.size += 1
        if self.value is None:
            self.value = value
        elif value < self.value:
            bst = BST(value)
            if self.left_child is None:
                self.left_child = bst
            else:
                self.left_child.insert(value)
        else:
            bst = BST(value)
            if self.right_child is None:
                self.right_child = bst
            else:
                self.right_child.insert(value)

    def delete(self, value):
        item = None
        if self.value == value:
            self.size -= 1
            if self.right_child is not None:
                self = self.left_child
            elif self.left_child is not None:
                self = self.right_child
            print(self.size)
        elif self.left_child is not None:
            before = self.left_child.size
            self.left_child.delete(value)
            after = self.left_child.size
            if after < before:
                self.size -= 1
                item = self.left_child
        elif self.right_child is not None:
            before = self.right_child.size
            self.right_child.delete(value)
            after = self.right_child.size
            item = self.right_child
            if after < before:
                self.size -= 1
                item = self.right_child
        if item is not None and item.size < 0:
            self.size -= 1
            del item


bst = BST()
bst.insert(10)
bst.insert(9)
bst.insert(8)
bst.insert(11)
bst.insert(13)
bst.delete(8)
bst.delete(13)

delattr()