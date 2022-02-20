# https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
 class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not (head and head.next):
            return None
        fast, slow = head, head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                slow = head
                while slow and slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None


