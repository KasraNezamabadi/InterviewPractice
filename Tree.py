import random


class Node:

    def __init__(self, value: int = None):
        self.left = None
        self.right = None
        self.value = value


def add_binary_tree(root: Node, value: int):
    if root.value > value:  # Must be added to left subtree

        if root.left is None:
            node_to_add = Node(value)
            root.left = node_to_add
        else:
            add_binary_tree(root.left, value)
    else:  # Must be added to right subtree
        if root.right is None:
            node_to_add = Node(value)
            root.right = node_to_add
        else:
            add_binary_tree(root.right, value)


def in_order_travers(root: Node):
    if root is not None:
        in_order_travers(root.left)
        print(root.value)  # Here we visit nodes
        in_order_travers(root.right)


def pre_order_travers(root: Node):
    if root is not None:
        print(root.value)
        pre_order_travers(root.left)
        pre_order_travers(root.right)


def post_order_travers(root: Node):
    if root is not None:
        pre_order_travers(root.left)
        pre_order_travers(root.right)
        print(root.value)


def depth_first_search(root: Node):
    stack = []
    stack.append(root)

    while len(stack) > 0:
        node = stack.pop()
        print(node.value)  # Here we visit nodes
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)


def depth_first_search_with_height(root: Node, balance_threshold=2):
    heights = []
    stack = []

    stack.append(root)
    stack.append(1)

    while len(stack) > 0:
        level = stack.pop()
        node = stack.pop()
        print(node.value)  # Here we visit nodes

        if node.left is None and node.right is None:  # node is a leaf
            heights.append(level)
        else:
            level += 1
        if node.right is not None:
            stack.append(node.right)
            stack.append(level)
        if node.left is not None:
            stack.append(node.left)
            stack.append(level)

    tree_height = max(heights)
    is_balanced = True
    diff = max(heights) - min(heights)
    if diff > balance_threshold or len(heights) == 1:
        is_balanced = False

    return tree_height, is_balanced


def breadth_first_search(root: Node):
    queue = []

    queue.append(root)
    while len(queue) > 0:
        node = queue[0]
        del queue[0]
        print(node.value)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)


my_list = []
a = None
b = None
my_list.append(a)
my_list.append(b)



input_list = [5, 3, 4, 8, 7, 9]  # Height of Binary tree depends on the order of the list
input_list = sorted(input_list)
root = Node(input_list[0])

for i in range(1, len(input_list)):
    add_binary_tree(root, input_list[i])

#in_order_travers(root)  # sorted list
#pre_order_travers(root)  # original list
#post_order_travers(root)
#depth_first_search(root)
#breadth_first_search(root)

#a, b = depth_first_search_with_height(root)
#print(a, b)

my_list = [(1, 75), (2, 60), (3, 80), (4, 65), (5, 90)]
aa = sorted(my_list, key=lambda item: item[1])
print(aa)

my_list = [1, 2, 3, 4, 5, 6]

#print(random.sample(my_list, 3))


randm_number = random.randint(0, 9)
#print(randm_number)

#print(random.randrange(10))



















