# Definition for singly-linked list.
from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.bubbleSortList(head, self.size(head) - 1, 0)

    def bubbleSortList(self, head: Optional[ListNode], row, col) -> Optional[ListNode]:
        if row == 0:
            return
        if col < row:
            first = self.get(head, col)
            second = self.get(head, col + 1)
            tail = self.gettail(head)

            if first.val > second.val:
                if first == head:
                    first = second
                    first.next = second.next
                    second.next = first
                elif second == tail:
                    prev = self.get(head, col - 1)
                    prev.next = second
                    tail = first
                    first.next = None
                    second.next = tail
                else:
                    prev = self.get(head, col - 1)
                    prev.next = second
                    first.next = second.next
                    second.next = first

            self.bubbleSortList(head, row, col + 1)
        else:
            self.bubbleSortList(head, row - 1, 0)

    def gettail(self, head):
        node = head
        while node.next:
            node = node.next
        return node

    def get(self, head, index):
        node = head
        for i in range(index):
            node = node.next
        return node

    def size(self, head):
        node = head
        count = 0
        while node:
            count += 1
            node = node.next
        return count

if __name__ == '__main__':
    from LinkedList import LinkedList
    l = LinkedList([10, 15, 5, 20, 25])
    l.printll()
    s = Solution()
    print(s.bubbleSortList(l.head, 5, 0))
