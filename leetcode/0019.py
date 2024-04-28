from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode(val=0, next=head)

        fastPtr = dummyNode
        for _ in range(n):
            fastPtr = fastPtr.next

        prevPtr, currPtr = None, dummyNode
        while fastPtr:
            fastPtr = fastPtr.next
            prevPtr, currPtr = currPtr, currPtr.next
        prevPtr.next = currPtr.next

        return dummyNode.next
