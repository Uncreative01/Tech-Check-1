class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    # Traversals
    def _in_order(self, node, result):
        if node:
            self._in_order(node.left, result)
            result.append(node.value)
            self._in_order(node.right, result)

    def _pre_order(self, node, result):
        if node:
            result.append(node.value)
            self._pre_order(node.left, result)
            self._pre_order(node.right, result)

    def _post_order(self, node, result):
        if node:
            self._post_order(node.left, result)
            self._post_order(node.right, result)
            result.append(node.value)

    def dean_msg(self, order):
        result = []

        if order == 'in':
            self._in_order(self.root, result)
        elif order == 'pre':
            self._pre_order(self.root, result)
        elif order == 'post':
            self._post_order(self.root, result)
        else:
            return "Invalid order. Use 'in', 'pre', or 'post'."

        return " ".join(result)


# ---- Build the tree ----

tree = BinaryTree()

#
#            programming
#           /            \
#       love              and
#      /    \               \
#   I      data            algorithms

tree.root = Node("programming")

tree.root.left = Node("love")
tree.root.right = Node("and")

tree.root.left.left = Node("I")
tree.root.left.right = Node("data")

tree.root.right.right = Node("algorithms")

# Input for User

def dean_msg(order):
    return tree.dean_msg(order)

order = input("Enter traversal order ('in', 'pre', or 'post'): ").strip().lower()

print("\nMessage to Dean:")
print(tree.dean_msg(order))