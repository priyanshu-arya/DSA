'''
https://leetcode.com/problems/linked-list-random-node/

'''


# Definition for singly-linked list.
from random import random


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


from typing import Optional


class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.n = 0
        self.head = head
        while head:
            self.n += 1
            head = head.next

    def getRandom(self) -> int:
        k = random.randint(0, self.n - 1) % self.n
        p = self.head

        while k > 0:
            p = p.next
            k -= 1

        return p.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()