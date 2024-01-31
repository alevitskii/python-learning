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
            s += str(node.val)
            node = node.next
        return s[::-1]


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def conver_to_number(head):
            node = head
            number = ""
            while node:
                number += str(node.val)
                node = node.next
            return int(number[::-1])

        def conver_to_list(number):
            prev = None
            number = str(number)
            idx = 0
            while idx < len(number):
                val = number[idx]
                node = ListNode(int(val), prev)
                prev = node
                idx += 1
            return prev

        return conver_to_list(conver_to_number(l1) + conver_to_number(l2))


class Solution2:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        head = None
        carrier = 0
        while l1 or l2 or carrier:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            val = l1Val + l2Val + carrier
            carrier = val > 9
            node = ListNode(val % 10)
            if prev:
                prev.next = node
            else:
                head = node
            prev = node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head


class Solution3:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        while l1 or l2 or carry:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            columnSum = l1Val + l2Val + carry
            carry = columnSum // 10
            newNode = ListNode(columnSum % 10)
            curr.next = newNode
            curr = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyHead.next


if __name__ == "__main__":
    inputs = [
        (ListNode(2, ListNode(4, (ListNode(3)))), ListNode(5, ListNode(6, ListNode(4)))),
        (ListNode(0), ListNode(0)),
        (
            ListNode(9, ListNode(9, (ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))),
            ListNode(9, ListNode(9, (ListNode(9, ListNode(9))))),
        ),
    ]
    s = Solution2()
    for l1, l2 in inputs:
        print(s.addTwoNumbers(l1, l2))
