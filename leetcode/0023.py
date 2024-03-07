from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        m = len(lists)
        if m == 0:
            return None
        if m == 1:
            return lists[0]

        list1 = self.mergeKLists(lists[: m // 2])
        list2 = self.mergeKLists(lists[m // 2:])
        return self.mergeTwoLists(list1, list2)

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        curr = dummy = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        curr.next = list1 if list1 else list2
        return dummy.next
