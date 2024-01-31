from math import inf


class Node:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


# T: O(n), S: O(n)
def is_valid(root, minv, maxv):
    if root is None:
        return True

    if minv < root.value < maxv:
        return is_valid(root.left, minv, root.value) and is_valid(root.right, root.value, maxv)
    return False


def is_valid_2(root):
    from math import inf

    def validate(node, minv, maxv):
        if node is None:
            return True

        if minv < node.value < maxv:
            return validate(node.left, minv, node.value) and validate(node.right, node.value, maxv)
        return False

    return validate(root, -inf, inf)


if __name__ == "__main__":
    inputs = [
        Node(12, left=Node(7, left=Node(5), right=Node(9)), right=Node(18, left=Node(16), right=Node(25))),
        Node(1),
        None,
    ]
    for root in inputs:
        print(is_valid(root, -inf, inf))
        print(is_valid_2(root))
