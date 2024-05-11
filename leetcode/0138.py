from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        table = {}
        currNode = head
        while currNode:
            table[currNode] = Node(currNode.val)
            currNode = currNode.next

        currNode = head
        while currNode:
            table[currNode].next = table.get(currNode.next)
            table[currNode].random = table.get(currNode.random)
            currNode = currNode.next

        return table[head]
