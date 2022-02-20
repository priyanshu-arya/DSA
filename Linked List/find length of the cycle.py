import LinkedList

class Solution:
    def find_cycle_length(self, head):
        fast, slow = head, head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                temp = slow.next
                leng = 1
                while temp != slow:
                    temp = temp.next
                    leng += 1
                return leng
