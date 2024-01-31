# 1 -> 2 -> 3 -> 4 -> 5 -> None ==> 5 -> 4 -> 3 -> 2 -> 1 -> None
# 1 -> None ==> 1 -> None
# None ==> None


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


# T: O(n), S: O(1)
def reverse_linked_list(head: Node):
    current = head
    prev = None
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next

    return prev


if __name__ == "__main__":
    inputs = [Node(1, Node(2, Node(3, Node(4, Node(5))))), Node(1), None]
    for head in inputs:
        print(head)
        print(reverse_linked_list(head))
