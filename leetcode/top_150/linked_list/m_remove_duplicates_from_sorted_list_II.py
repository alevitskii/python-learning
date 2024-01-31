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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        dummy = ListNode(0, head)
        before_segment = dummy
        prev = None
        node = head
        segment_start = head
        skip_segment = False
        while node:
            if prev and node.val == prev.val:
                skip_segment = True
            elif prev and node.val != prev.val:
                if not skip_segment:
                    before_segment.next = segment_start
                    before_segment = prev
                skip_segment = False
                segment_start = node
            prev = node
            node = node.next
        before_segment.next = None if skip_segment else segment_start
        return dummy.next


class Solution2:
    def deleteDuplicates(self, head):
        fake = ListNode(-1)
        fake.next = head
        # We use prev (for node just before duplications begins), curr (for the last node of the duplication group)...
        curr, prev = head, fake
        while curr:
            # while we have curr.next and its value is equal to curr...
            # It means, that we have one more duplicate...
            while curr.next and curr.val == curr.next.val:
                # So move curr pointer to the right...
                curr = curr.next
            # If it happens, that prev.next equal to curr...
            # It means, that we have only 1 element in the group of duplicated elements...
            if prev.next == curr:
                # Don't need to delete it, we move both pointers to right...
                prev = prev.next
                curr = curr.next
            # Otherwise, we need to skip a group of duplicated elements...
            # set prev.next = curr.next, and curr = prev.next...
            else:
                prev.next = curr.next
                curr = prev.next
        # Return the linked list...
        return fake.next


if __name__ == "__main__":
    inputs = [
        ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5))))))),
        ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(3))))),
        ListNode(1, ListNode(1, ListNode(3, ListNode(2, ListNode(2))))),
        ListNode(1),
        None,
    ]
    s = Solution2()
    for head in inputs:
        print(s.deleteDuplicates(head))
