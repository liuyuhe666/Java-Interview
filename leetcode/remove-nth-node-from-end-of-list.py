from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        p1 = dummy
        p2, p3 = head, head
        for i in range(n):
            p3 = p3.next
        while p3 is not None:
            p1 = p1.next
            p2 = p2.next
            p3 = p3.next
        p1.next = p2.next
        return dummy.next
