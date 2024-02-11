from typing import Optional


# Definition for singly-linked list.
class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None
        old_to_new = {}
        node = head
        while node:
            old_to_new[node] = Node(node.val)
            node = node.next
        node = head
        while node:
            old_to_new[node].next = old_to_new[node.next] if node.next is not None else None
            old_to_new[node].random = old_to_new[node.random] if node.random is not None else None
            node = node.next
        return old_to_new[head]


class Solution2:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None

        curr = head
        while curr:
            new_node = Node(curr.val, curr.next)
            curr.next = new_node
            curr = new_node.next

        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        old_head = head
        new_head = head.next
        curr_old = old_head
        curr_new = new_head

        while curr_old:
            curr_old.next = curr_old.next.next
            curr_new.next = curr_new.next.next if curr_new.next else None
            curr_old = curr_old.next
            curr_new = curr_new.next

        return new_head


class Solution3:
    def __init__(self):
        self.visited = {}

    def copyRandomList(self, head: Node) -> Node:
        if not head:
            return None

        if head in self.visited:
            return self.visited[head]

        newNode = Node(head.val)
        self.visited[head] = newNode

        newNode.next = self.copyRandomList(head.next)
        newNode.random = self.copyRandomList(head.random)

        return newNode


def main() -> None:
    node1 = Node(7)
    node2 = Node(13)
    node3 = Node(11)
    node4 = Node(10)
    node5 = Node(1)
    node1.next = node2
    node2.next = node3
    node2.random = node1
    node3.next = node4
    node3.random = node5
    node4.next = node5
    node4.random = node3
    node5.random = node1
    inputs = [node1]
    s = Solution2()
    for head in inputs:
        print(s.copyRandomList(head))


if __name__ == "__main__":
    main()
