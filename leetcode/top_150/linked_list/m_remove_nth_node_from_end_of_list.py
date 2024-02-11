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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes_list = []
        node = head
        while node:
            nodes_list.append(node)
            node = node.next
        if len(nodes_list) == 1:
            return None
        idx = len(nodes_list) - n
        if idx - 1 < 0:
            return nodes_list[idx + 1]
        elif idx + 1 > len(nodes_list) - 1:
            nodes_list[idx - 1].next = None
            return head
        else:
            nodes_list[idx - 1].next = nodes_list[idx + 1]
            return head


class Solution2:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast = head, head
        number_of_nodes = 1
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            number_of_nodes += 2
        number_of_nodes -= fast is None
        # 1 nodes: slow at 1nd node, 0 idx
        # 2 nodes: slow at 2nd node, 1 idx
        # 3 nodes: slow at 2nd node, 1 idx
        # 4 nodes: slow at 3nd node, 2 idx
        # 5 nodes: slow at 3nd node, 2 idx
        if number_of_nodes == 1:
            return None
        slow_idx = number_of_nodes // 2
        idx_to_del = number_of_nodes - n
        if idx_to_del == 0:
            return head.next
        if slow_idx >= idx_to_del:
            slow = head
            slow_idx = 0
        while slow_idx < idx_to_del - 1:
            slow = slow.next
            slow_idx += 1
        slow.next = slow.next.next
        return head


class Solution3:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = head
        slow = head
        # advance fast to nth position
        for i in range(n):
            fast = fast.next

        if not fast:
            return head.next
        # then advance both fast and slow now they are nth postions apart
        # when fast gets to None, slow will be just before the item to be deleted
        while fast.next:
            slow = slow.next
            fast = fast.next
        # delete the node
        slow.next = slow.next.next
        return head


def main() -> None:
    inputs = [
        (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2),
        (ListNode(1), 1),
        (
            ListNode(
                1,
                ListNode(
                    2,
                ),
            ),
            2,
        ),
        (ListNode(1, ListNode(2, ListNode(3))), 3),
    ]
    s = Solution()
    for head, n in inputs:
        print(s.removeNthFromEnd(head, n))


if __name__ == "__main__":
    main()
