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
        map_ = {}
        node = head
        while node:
            map_[node] = Node(node.val)
            node = node.next
        node = head
        while node:
            map_[node].next = map_.get(node.next)
            map_[node].random = map_.get(node.random)
            node = node.next
        return map_[head]


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


if __name__ == "__main__":
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
