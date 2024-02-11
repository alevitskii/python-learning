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
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before, after = ListNode(0), ListNode(0)
        before_curr, after_curr = before, after

        while head:
            if head.val < x:
                before_curr.next, before_curr = head, head
            else:
                after_curr.next, after_curr = head, head
            head = head.next

        after_curr.next = None
        before_curr.next = after.next

        return before.next


def main() -> None:
    inputs = [
        (ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2)))))), 3),
        (ListNode(2, ListNode(1)), 2),
    ]
    s = Solution()
    for head, x in inputs:
        print(s.partition(head, x))


if __name__ == "__main__":
    main()
