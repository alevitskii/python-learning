from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        node = self
        s = ""
        while node:
            s += f"{node.val} --> "
            node = node.next
        return s + "None"


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        node = head
        before_start = ListNode(0, head)
        position = 1
        while position < left:
            before_start = node
            node = node.next
            position += 1
        prev = None
        future_tail = node
        while position <= right:
            next = node.next
            node.next = prev
            prev = node
            node = next
            position += 1
        before_start.next = prev
        future_tail.next = node
        return before_start.next if left == 1 else head


def main() -> None:
    inputs = [
        (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2, 4),
        (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 1, 4),
        (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2, 5),
        (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 1, 5),
        (ListNode(5), 1, 1),
    ]
    s = Solution()
    for head, left, right in inputs:
        print(s.reverseBetween(head, left, right))


if __name__ == "__main__":
    main()
