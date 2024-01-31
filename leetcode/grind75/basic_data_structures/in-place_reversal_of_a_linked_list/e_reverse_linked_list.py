from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev, next_ = head, head.next
        prev.next = None
        while next_ is not None:
            tmp = next_.next
            next_.next = prev
            prev, next_ = next_, tmp
        return prev


if __name__ == "__main__":
    inputs = [ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), ListNode(1, ListNode(2)), None]
    s = Solution()
    for head in inputs:
        print(s.reverseList(head))
