# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        mid = self.getmidlist(head)
        left = self.sortList(head)
        right = self.sortList(mid)

        return self.merge(left, right)

    def merge(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 or list2

        if list1.val < list2.val:
            list1.next = self.merge(list1.next, list2)
            return list1
        else:
            list2.next = self.merge(list1, list2.next)
            return list2

    def getmidlist(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head.next, head

        while fast != None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        start = slow.next
        slow.next = None
        return start


from LinkedList import LinkedList

s = Solution()
l = LinkedList([10, 15, 5, 20, 25])
s.sortList(l.head)
l.printll()
