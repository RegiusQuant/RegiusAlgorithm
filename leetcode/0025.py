from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = last = ListNode(0, head)

        while head:
            tail = self.getGroupTail(head, k)
            if tail is None:
                break

            stop = tail.next
            self.reverseList(head, stop)

            last.next = tail
            head.next = stop

            last = head
            head = stop

        return dummy.next

    def getGroupTail(self, head: ListNode, k: int) -> Optional[ListNode]:
        while head:
            k -= 1
            if k == 0:
                return head
            head = head.next
        return None

    def reverseList(self, head: ListNode, stop: ListNode):
        last = head
        head = head.next
        while head != stop:
            temp = head.next
            head.next = last
            last = head
            head = temp
