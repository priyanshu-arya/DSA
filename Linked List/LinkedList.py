"""
Node class
Every Node in the class is represented by this Node
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# Create Linked List Class


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        self.lenl = 0

        if nodes is not None:
            node = Node(val=nodes.pop(0))
            self.head = node
            self.lenl += 1
            for ele in nodes:
                node.next = Node(val=ele)
                node = node.next
                self.lenl += 1


    def printll(self):
        head = self.head
        while head:
            print(head.val, end='->')
            head = head.next
        print('None')

    def lenll(self):
        return self.lenl

    def insert(self, data, pos:int):
        if -1 > pos or pos > self.lenl+1:
            raise 'Position is far then range'

        if pos == 0:
            newN = Node(val=data)
            newN.next = self.head
            self.head = newN
            self.lenl += 1
            return self.head

        temp = self.head
        while pos > 2:
            temp = temp.next
            pos -= 1

        newt = Node(val=data)
        newt.next = temp.next
        temp.next = newt
        self.lenl += 1

        return self.head

    def insertLeft(self, data):
        newN = Node(val=data)
        newN.next = self.head
        self.head = newN
        self.lenl += 1
        return self.head

    def insertRight(self, data):
        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = Node(data)
        self.lenl += 1
        return self.head

    def delete(self, pos):
        # if pos in our range
        if -1 < pos < self.lenl+1:

            # if pos is first
            if pos == 0:
                self.head = self.head.next
                self.lenl -= 1
                return self.head

            temp = self.head

            # if pos is last
            if pos == self.lenl:
                while temp.next.next:
                    temp = temp.next
                temp.next = None
                self.lenl -= 1
                return self.head

            # if pos in between our range

            while pos > 2:
                temp = temp.next
                pos -= 1

            temp.next = temp.next.next
            self.lenl -= 1
            return self.head
        else:
            raise 'Position not in range'

    def deleteLeft(self):
        if self.lenl == 0:
            print('List Underflow')
            return
        self.head = self.head.next
        self.lenl -= 1
        return self.head

    def deleteRight(self):
        if self.lenl == 0:
            print('List Underflow')
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None
        self.lenl -= 1
        return self.head






if __name__ == "__main__":
    list = [1, 2, 3, 4, 5, 6]
    llist = LinkedList(list)
    llist.printll()
    print(llist.lenll())
    llist.insert(7, 0)
    llist.printll()
    llist.insert(8, 8)
    llist.printll()
    llist.insertLeft(10)
    llist.printll()
    llist.insertRight(11)
    llist.printll()
    print(llist.lenll())
    llist.delete(9)
    print(llist.lenll())
    llist.printll()
    llist.deleteLeft()
    print(llist.lenll())
    llist.printll()
    llist.deleteRight()
    print(llist.lenll())
    llist.printll()


