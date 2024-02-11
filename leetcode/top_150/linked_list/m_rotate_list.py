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
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        slow, fast = head, head
        length = 0
        while k > 0:
            fast = fast.next
            k -= 1
            length += 1
            if fast is None:
                k %= length
                fast = head
        if fast == head:
            return head
        while fast.next:
            slow = slow.next
            fast = fast.next
        new_head = slow.next
        fast.next = head
        slow.next = None
        return new_head


class Solution2:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        lastElement = head
        length = 1
        # get the length of the list and the last node in the list
        while lastElement.next:
            lastElement = lastElement.next
            length += 1
        # If k is equal to the length of the list then k == 0
        # ElIf k is greater than the length of the list then k = k % length
        k = k % length
        # Set the last node to point to head node
        # The list is now a circular linked list with last node pointing to first node
        lastElement.next = head
        # Traverse the list to get to the node just before the ( length - k )th node.
        # Example: In 1->2->3->4->5, and k = 2
        #          we need to get to the Node(3)
        tempNode = head
        for _ in range(length - k - 1):
            tempNode = tempNode.next
        # Get the next node from the tempNode and then set the tempNode.next as None
        # Example: In 1->2->3->4->5, and k = 2
        #          tempNode = Node(3)
        #          answer = Node(3).next => Node(4)
        #          Node(3).next = None ( cut the linked list from here )
        answer = tempNode.next
        tempNode.next = None
        return answer


def main() -> None:
    inputs = [
        (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2),
        (ListNode(0, ListNode(1, ListNode(2))), 4),
        (ListNode(0, ListNode(1)), 3),
        (ListNode(0, ListNode(1, ListNode(2))), 2000000000),
    ]
    s = Solution()
    for head, k in inputs:
        print(s.rotateRight(head, k))


if __name__ == "__main__":
    main()
