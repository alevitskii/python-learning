from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head, current = None, None
        while list1 and list2:
            if list1.val < list2.val:
                if current:
                    current.next = list1
                current, list1 = list1, list1.next
            else:
                if current:
                    current.next = list2
                current, list2 = list2, list2.next
            head = head or current
        if list1:
            if current:
                current.next = list1
            head = head or list1
        elif list2:
            if current:
                current.next = list2
            head = head or list2
        return head


class Solution2:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        prev = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next
        prev.next = list1 if list1 else list2
        return dummy.next


if __name__ == "__main__":
    inputs = [
        (ListNode(1, ListNode(2, ListNode(4))), ListNode(1, ListNode(3, ListNode(4)))),
        (None, None),
        (None, ListNode(0)),
    ]

    s = Solution2()
    for list1, list2 in inputs:
        print(s.mergeTwoLists(list1, list2))
