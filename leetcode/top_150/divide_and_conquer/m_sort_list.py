from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge(self, node1, node2):
        head = tail = ListNode()
        while node1 and node2:
            if node1.val > node2.val:
                tail.next = node2
                node2 = node2.next
            else:
                tail.next = node1
                node1 = node1.next
            tail = tail.next
        if node1:
            tail.next = node1
        elif node2:
            tail.next = node2
        return head.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        slow.next, slow = None, slow.next
        return self.merge(self.sortList(head), self.sortList(slow))


if __name__ == "__main__":
    inputs = [
        ListNode(4, ListNode(2, ListNode(1, ListNode(3)))),
        ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0))))),
        ListNode(3, ListNode(2, ListNode(4))),
    ]
    s = Solution()
    for head in inputs:
        head = s.sortList(head)
        print(head)
