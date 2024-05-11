from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def mergeList(head1: ListNode, head2: ListNode) -> ListNode:
            curr = dummy = ListNode()

            temp1, temp2 = head1, head2
            while temp1 and temp2:
                if temp1.val < temp2.val:
                    curr.next = temp1
                    temp1 = temp1.next
                else:
                    curr.next = temp2
                    temp2 = temp2.next
                curr = curr.next
            curr.next = temp1 if temp1 else temp2

            return dummy.next

        def mergeSort(head: ListNode, tail: ListNode) -> ListNode:
            if not head:
                return head
            if head.next == tail:
                head.next = None
                return head

            slow = fast = head
            while fast != tail:
                slow = slow.next
                fast = fast.next
                if fast != tail:
                    fast = fast.next

            head1, head2 = mergeSort(head, slow), mergeSort(slow, tail)
            return mergeList(head1, head2)

        return mergeSort(head, None)
