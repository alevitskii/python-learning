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
        dummy = ListNode()
        prev = dummy
        while list1 and list2:
            if list1.val < list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next
        if list1:
            prev.next = list1
        if list2:
            prev.next = list2
        return dummy.next


def main() -> None:
    node11 = ListNode(1)
    node12 = ListNode(2)
    node13 = ListNode(4)
    node11.next = node12
    node12.next = node13
    node21 = ListNode(1)
    node22 = ListNode(3)
    node23 = ListNode(4)
    node21.next = node22
    node22.next = node23
    inputs = [(node11, node21)]
    s = Solution2()
    for head1, head2 in inputs:
        print(s.mergeTwoLists(head1, head2))


if __name__ == "__main__":
    main()
