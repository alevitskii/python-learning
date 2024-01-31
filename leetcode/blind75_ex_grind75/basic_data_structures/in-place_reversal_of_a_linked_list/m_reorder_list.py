from typing import Optional, Self


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next: Optional[Self] = None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None or head.next.next is None:
            return
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        current = slow.next
        prev = None
        slow.next = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        first, second = head, prev
        while second:
            second_next = second.next
            second.next = first.next
            first.next = second
            second = second_next
            first = first.next.next


class Solution2:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        first, second = head, prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next


if __name__ == "__main__":
    inputs = [
        ListNode(1, ListNode(2, ListNode(3, ListNode(4)))),
        ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))),
        ListNode(1, ListNode(2, ListNode(3))),
    ]
    s = Solution()
    for head in inputs:
        print(s.reorderList(head))
