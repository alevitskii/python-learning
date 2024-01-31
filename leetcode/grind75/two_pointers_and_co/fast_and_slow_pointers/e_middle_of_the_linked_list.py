from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow


if __name__ == "__main__":
    inputs = [
        ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))),
        ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))),
    ]

    s = Solution()
    for head in inputs:
        print(s.middleNode(head))
