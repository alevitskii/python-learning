# 1---2---3---4---5---6
#     |           |
#     7---8---9   12---13   ===>   1---2---7---8---10---11---9---3---4---5---12---13---6
#             |
#             10---11


class Node:
    def __init__(self, value, next=None, prev=None, child=None):
        self.value = value
        self.next = next
        self.prev = prev
        self.child = child

    def __str__(self):
        s = ""
        node = self.next
        while node:
            s += f"{node.value} -> "
            node = node.next
        return f"{self.value} -> " + s + "None"


# T: O(n), S: O(1)
def flatten(head):
    node = head
    prev = None

    while node:
        if node.child is not None:
            next = node.next
            if next is not None:
                tail = flatten(node.child)
                node.next = node.child
                node.child.prev = node
                node.child = None
                tail.next = next
                next.prev = tail
                node = tail.next
            else:
                node.next = node.child
                node.child = None
                node.next.prev = node
                prev = node
                node = node.next
        else:
            prev = node
            node = node.next

    return prev


# T: O(2n) ~= O(n), S: O(1)
def flatten2(head):
    if head is None:
        return head

    current_node = head
    while current_node:
        if current_node.child is None:
            current_node = current_node.next
        else:
            tail = current_node.child
            while tail.next:
                tail = tail.next
            tail.next = current_node.next
            if tail.next:
                tail.next.prev = tail
            current_node.next = current_node.child
            current_node.next.prev = current_node
            current_node.child = None

    return head


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    node9 = Node(9)
    node10 = Node(10)
    node11 = Node(11)
    node12 = Node(12)
    node13 = Node(13)

    # Level 1
    node1.next = node2
    node2.prev = node1
    node2.next = node3
    node2.child = node7
    node3.prev = node2
    node3.next = node4
    node4.prev = node3
    node4.next = node5
    node5.prev = node4
    node5.next = node6
    node5.child = node12
    node6.prev = node5
    # Level 2
    node7.next = node8
    # node7.child = node10
    node8.prev = node7
    node8.next = node9
    # node8.child = node10
    node9.prev = node8
    node9.child = node10
    node12.next = node13
    node13.prev = node12
    # Level 3
    node10.next = node11
    node11.prev = node10

    inputs = [node1]
    for head in inputs:
        # flatten2(head)
        # print(head)
        print(flatten2(head))
