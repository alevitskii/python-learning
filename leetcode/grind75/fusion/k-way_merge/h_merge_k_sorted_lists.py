from itertools import zip_longest
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge(self, list1, list2):
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
        if list1:
            prev.next = list1
        else:
            prev.next = list2
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 1 and not lists[0]:
            return None
        merged = []
        while len(lists) > 1:
            for list1, list2 in zip_longest(lists[::2], lists[1::2]):
                merged.append(self.merge(list1, list2))
            lists = merged
            merged = []
        return lists[0]


class Solution2:
    def merge(self, list1, list2):
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
        if list1:
            prev.next = list1
        else:
            prev.next = list2
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) > 0:
            step = 1
            while step < len(lists):
                for i in range(0, len(lists) - step, step * 2):
                    lists[i] = self.merge(lists[i], lists[i + step])
                step *= 2
            return lists[0]
        return


if __name__ == "__main__":
    inputs = [
        [ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))],
        [
            ListNode(1, ListNode(4, ListNode(5))),
            ListNode(1, ListNode(3, ListNode(4))),
            ListNode(2, ListNode(6)),
            ListNode(4, ListNode(8)),
        ],
        [],
        [[]],
    ]

    s = Solution2()
    for lists in inputs:
        print(s.mergeKLists(lists))
