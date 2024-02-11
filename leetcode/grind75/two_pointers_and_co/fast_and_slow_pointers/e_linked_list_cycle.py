from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# https://en.wikipedia.org/wiki/Cycle_detection
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

            if slow.val == fast.val:
                return True

        return False


def main() -> None:
    node11 = ListNode(3)
    node12 = ListNode(2)
    node13 = ListNode(0)
    node14 = ListNode(-4)
    node11.next = node12
    node12.next = node13
    node13.next = node14
    node14.next = node12

    node21 = ListNode(1)
    node22 = ListNode(2)
    node21.next = node22
    node22.next = node21

    node31 = ListNode(1)
    inputs = [node11, node21, node31]

    s = Solution()
    for head in inputs:
        print(s.hasCycle(head))


if __name__ == "__main__":
    main()
