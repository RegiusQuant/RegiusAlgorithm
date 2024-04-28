from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(0, head)

        prevNode = dummyNode
        while prevNode.next and prevNode.next.next:
            currNode, nextNode = prevNode.next, prevNode.next.next
            prevNode.next = nextNode
            currNode.next = nextNode.next
            nextNode.next = currNode
            prevNode = currNode

        return dummyNode.next
