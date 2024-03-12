import heapq
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        setattr(ListNode, "__lt__", lambda self, other: self.val < other.val)

        h = []
        for node in lists:
            if node:
                heapq.heappush(h, node)

        curr = dummy = ListNode()
        while h:
            node = heapq.heappop(h)
            curr.next = ListNode(node.val)
            curr = curr.next

            node = node.next
            if node:
                heapq.heappush(h, node)

        return dummy.next
