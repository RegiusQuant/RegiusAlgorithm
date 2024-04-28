from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slowPtr, fastPtr = head, head
        while fastPtr and fastPtr.next:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
            if slowPtr == fastPtr:
                currPtr = head
                while currPtr != slowPtr:
                    currPtr, slowPtr = currPtr.next, slowPtr.next
                return currPtr
        return None
