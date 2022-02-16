class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoublyLL:
    def __init__(self, nodes=None):
        self.head = None
        self.lenl = 0

        if nodes is not None:
            node = Node(val=nodes.pop(0))
            self.head = node
            self.lenl += 1
            for ele in nodes:
                node.next = Node(val=ele)
                node.next.prev = node
                node = node.next
                self.lenl += 1

    def insertF(self, data):
        if self.lenl == 0:
            self.head = Node(val=data)
            self.lenl += 1
        else:
            node = Node(val=data)
            self.head.prev = node
            node.next = self.head
            self.head = node

    def insertRight(self, data):
        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = Node(data)
        temp.next.prev = temp
        self.lenl += 1
        return self.head

    def printll(self):
        head = self.head
        while head:
            print(head.val, end="->")
            head = head.next
        print('None')


if __name__ == "__main__":
    list = [1, 2, 3, 4, 5, 6]
    dlist = DoublyLL(list)
    dlist.insertF(1)
    dlist.insertRight(2)
    dlist.printll()
