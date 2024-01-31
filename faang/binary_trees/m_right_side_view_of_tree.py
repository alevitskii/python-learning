class Node:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


# Node(1, left=Node(2, left=Node(4, right=Node(7, left=Node(8))), right=Node(5)), right=Node(3, right=Node(6))) ==>
# [1, 3, 6, 7, 8]
# None ==> []
# Node(1) ==> [1]


# T: O(n), S: O(n) (Θ(w) - width)
def right_side_view_bfs(node):
    if node is None:
        return []
    queue = [node]
    result = []
    while queue:
        length, count = len(queue), 0
        while count < length:
            node = queue.pop(0)
            count += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(node.value)
    return result


# T: O(n), S: O(n) (Θ(h) - height of the tree)
def right_side_view_dfs(node):
    result = []
    max_depth = 0

    def traverse_pre_order(node, current_depth):
        nonlocal max_depth
        if node is None:
            return
        if current_depth > max_depth:
            result.append(node.value)
            max_depth = current_depth
        if node.right:
            traverse_pre_order(node.right, current_depth + 1)
        if node.left:
            traverse_pre_order(node.left, current_depth + 1)

    traverse_pre_order(node, 1)
    return result


def right_side_view_dfs_2(node):
    result = []

    def traverse_pre_order(node, current_level):
        if node is None:
            return
        if current_level >= len(result):
            result.append(node.value)
        if node.right:
            traverse_pre_order(node.right, current_level + 1)
        if node.left:
            traverse_pre_order(node.left, current_level + 1)

    traverse_pre_order(node, 0)
    return result


if __name__ == "__main__":
    inputs = [
        Node(1, left=Node(2, left=Node(4, right=Node(7, left=Node(8))), right=Node(5)), right=Node(3, right=Node(6))),
        Node(1),
        None,
    ]

    for root in inputs:
        print(right_side_view_bfs(root))
        print(right_side_view_dfs(root))
        print(right_side_view_dfs_2(root))
