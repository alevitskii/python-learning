class Node:
    def __init__(self, value=None, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


# T: O(n), S: O(h) (h - height of the tree: perfectly balanced tree - O(logn), linked list like - O(n)
def max_tree_depth(node: Node):
    if node is None:
        return 0
    return 1 + max(max_tree_depth(node.left), max_tree_depth(node.right))


if __name__ == "__main__":
    inputs = [
        Node(left=Node(left=Node(right=Node(right=Node()))), right=Node()),
        Node(right=Node(right=Node(right=Node(right=Node())))),
        Node(),
        None,
    ]
    for root in inputs:
        print(max_tree_depth(root))
