class Node:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


# Node(3, left=Node(6, left=Node(9, right=Node(5, left=Node(8))), right=Node(2)), right=Node(1, right=Node(4))) ==>
# [[3], [6, 1], [9, 2, 4], [5], [8]]
# Node(3) ==> [[3]]
# None ==> []


# T: O(n), S: O(n) + O(n/2) (full binary tree) ~ O(n)
def level_order_traversal(node):
    if node is None:
        return []
    queue = [node]
    result = []
    child_queue = []
    temp = []
    while queue:
        node = queue.pop(0)
        temp.append(node.value)
        if node.left:
            child_queue.append(node.left)
        if node.right:
            child_queue.append(node.right)
        if not queue:
            queue = child_queue
            child_queue = []
            result.append(temp)
            temp = []
    return result


# T: O(n), S: ~O(n)
def level_order_traversal_2(node):
    if node is None:
        return []
    queue = [node]
    result = []
    while queue:
        length, count = len(queue), 0
        level_values = []
        while count < length:
            node = queue.pop(0)
            level_values.append(node.value)
            count += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level_values)
    return result


if __name__ == "__main__":
    inputs = [
        Node(3, left=Node(6, left=Node(9, right=Node(5, left=Node(8))), right=Node(2)), right=Node(1, right=Node(4))),
        Node(3),
        None,
    ]
    for root in inputs:
        print(level_order_traversal(root))
        print(level_order_traversal_2(root))
