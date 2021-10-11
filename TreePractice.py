class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def get_value(self):
        return self.value


class NodeStack:

    def __init__(self):
        self._stack_list: [Node] = []

    def push_node(self, node: Node):
        if node is not None:
            self._stack_list.append(node)

    def pop_node(self):
        return self._stack_list.pop()

    def has_value(self):
        if len(self._stack_list) > 0:
            return True
        return False


def binary_insert(root: Node, value: int):

    if value < root.get_value():  # should be inserted in the left subtree
        if root.get_left_child() is None:
            root.left = Node(value)
        else:
            binary_insert(root.get_left_child(), value)
    else:
        if root.get_right_child() is None:
            root.right = Node(value)
        else:
            binary_insert(root.get_right_child(), value)


def in_order_travers(root: Node):
    if root is not None:
        in_order_travers(root.get_left_child())
        visit(root)
        in_order_travers(root.get_right_child())


def visit(node: Node):
    print(node.get_value())


def depth_first_search(root: Node):
    nodeStack = NodeStack()
    nodeStack.push_node(root)

    while nodeStack.has_value():
        node = nodeStack.pop_node()
        visit(node)
        right_child = node.right
        left_child = node.left
        nodeStack.push_node(right_child)
        nodeStack.push_node(left_child)


def check_bst(root: Node):
    if root.left is not None:
        if root.value < root.left.value:
            return False
        check_bst(root.left)

    if root.right is not None:
        if root.value > root.right.value:
            return False
        check_bst(root.right)


temp_root = Node(4)
binary_insert(temp_root, 2)
binary_insert(temp_root, 1)
binary_insert(temp_root, 3)
binary_insert(temp_root, 6)
binary_insert(temp_root, 5)

result = check_bst(root=temp_root)

if result is None:
    print('Tree is BST')
else:
    print('Tree is Not BST')



a = 'ab'
b = 'ac1234 ' \
    ''

print(a > b)

#depth_first_search(temp_root)

#in_order_travers(temp_root)








