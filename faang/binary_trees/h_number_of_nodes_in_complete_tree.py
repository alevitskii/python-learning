from math import ceil


class Node:
    def __init__(self, value=None, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


def get_tree_height(node):
    height = 0
    while node.left is not None:
        height += 1
        node = node.left
    return height


def node_exists(idx_to_find, height, node):
    left, right = 0, 2**height - 1
    count = 0

    while count < height:
        mid_of_node = ceil((left + right) / 2)
        if idx_to_find >= mid_of_node:
            node = node.right
            left = mid_of_node
        else:
            node = node.left
            right = mid_of_node - 1
        count += 1
    return node is not None


# T: O(h + h**2) ~ O(log^2(n)), S: O(1)
def number_of_nodes(root):
    if root is None:
        return 0

    height = get_tree_height(root)
    if height == 0:
        return 1

    upper_count = 2**height - 1
    left, right = 0, upper_count
    while left < right:
        idx_to_find = ceil((left + right) / 2)
        if node_exists(idx_to_find, height, root):
            left = idx_to_find
        else:
            right = idx_to_find - 1

    return upper_count + left + 1


if __name__ == "__main__":
    inputs = [
        Node(
            left=Node(left=Node(left=Node(), right=Node()), right=Node(left=Node(), right=Node())),
            right=Node(left=Node(left=Node()), right=Node()),
        )
    ]
    for root in inputs:
        print(number_of_nodes(root))
