class Node:
    def __init__(self, value: int = None, parent=None):
        self.parent: Node = parent
        self.left: Node = None
        self.right: Node = None
        self.value = value


class MinHeap:
    def __init__(self, value: int):
        self.root = Node(value)
        self.leaf_to_add = Node(value=None, parent=self.root)

    def insert(self, value: int):
        self.leaf_to_add.value = value
        parent = self.leaf_to_add.parent

        if parent.left is None:
            parent.left = self.leaf_to_add
        else:
            parent.right = self.leaf_to_add

        while parent is not None:
            if parent.value > self.leaf_to_add.value:
                parent.value, self.leaf_to_add.value = self.leaf_to_add.value, parent.value
            parent = parent.parent

        parent = self.leaf_to_add.parent
        if parent.right is None:
            self.leaf_to_add = Node(value=None, parent=parent)
        else:
            self.leaf_to_add = Node(value=None, parent=self.leaf_to_add)


min_heap = MinHeap(4)
min_heap.insert(3)
min_heap.insert(2)
min_heap.insert(8)

v = 9






