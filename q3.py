class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None


tree = BinaryTree()

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


# ---- ASCII Tree Printer ----
def ascii_tree(tree):
    def _print_tree(node, prefix="", is_left=True):
        if node is not None:
            if node.right:
                _print_tree(node.right, prefix + ("│   " if is_left else "    "), False)

            print(prefix + ("└── " if is_left else "┌── ") + node.value)

            if node.left:
                _print_tree(node.left, prefix + ("    " if is_left else "│   "), True)

    if tree.root is None:
        print("Tree is empty.")
    else:
        _print_tree(tree.root)


# ---- Input ----
choice = input("Would you like to display the Binary Tree? (yes/no): ").strip().lower()

if choice == "yes":
    print("\nASCII Binary Tree:\n")
    ascii_tree(tree)
else:
    print("Tree display skipped.")
