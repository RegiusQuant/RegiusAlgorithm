from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []

        currNode = head
        while currNode:
            values.append(currNode.val)
            currNode = currNode.next

        return values == values[::-1]
