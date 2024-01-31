# 1 -> 2 -> 3 -> 4 -> 5 -> None, m = 2, n = 4 ==> 1 -> 4 -> 3 -> 2 -> 5 -> None
# 1 -> 2 -> 3 -> 4 -> 5 -> None, m = 1, n = 5 ==> 5 -> 4 -> 3 -> 2 -> 1 -> None
# 1 -> None, m = 1, n = 1 ==> 1 -> None
# None, m = 0, n = 0 ==> None


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        s = ""
        node = self.next
        while node:
            s += f"{node.value} -> "
            node = node.next
        return f"{self.value} -> " + s + "None"


def reverse_between(head, m, n):
    if head is None:
        return

    current_position = 1
    current_node = head
    start = head
    while current_position < m:
        start = current_node
        current_node = current_node.next
        current_position += 1

    new_list, tail = None, current_node

    while m <= current_position <= n:
        next = current_node.next
        current_node.next = new_list
        new_list = current_node
        current_node = next
        current_position += 1

    start.next = new_list
    tail.next = current_node

    return head if m > 1 else new_list


if __name__ == "__main__":
    inputs = [
        (Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8)))))))), 3, 6),
        (Node(1, Node(2, Node(3, Node(4, Node(5))))), 2, 4),
        (Node(1, Node(2, Node(3, Node(4, Node(5))))), 1, 5),
        (Node(1), 1, 1),
        (Node(3, Node(5)), 1, 1),
        (None, 0, 0),
    ]
    for head, m, n in inputs:
        print(head, m, n)
        print(reverse_between(head, m, n))
