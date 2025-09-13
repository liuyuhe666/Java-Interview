from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        carry = 0
        p = dummy
        while l1 is not None and l2 is not None:
            num = l1.val + l2.val + carry
            carry = num // 10
            node = ListNode(num % 10, None)
            p.next = node
            p = p.next
            l1 = l1.next
            l2 = l2.next
        while l1 is not None:
            num = l1.val + carry
            carry = num // 10
            node = ListNode(num % 10, None)
            p.next = node
            p = p.next
            l1 = l1.next
        while l2 is not None:
            num = l2.val + carry
            carry = num // 10
            node = ListNode(num % 10, None)
            p.next = node
            p = p.next
            l2 = l2.next
        if carry != 0:
            node = ListNode(carry, None)
            p.next = node
            p = p.next
        return dummy.next
