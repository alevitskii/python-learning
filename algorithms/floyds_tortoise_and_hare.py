class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# T: O(n), S: O(1)
def find_cycle_p(head):
    slow, fast = head, head

    while True:
        slow = slow.next
        fast = fast.next
        if fast is None or fast.next is None:
            return False
        fast = fast.next
        if slow == fast:
            break
    p1 = head
    p2 = slow

    while p1 != p2:
        p1 = p1.next
        p2 = p2.next

    # this is the node where the cycle begins
    return p1


def main() -> None:
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node8
    node8.next = node3

    print(find_cycle_p(node1))


if __name__ == "__main__":
    main()
