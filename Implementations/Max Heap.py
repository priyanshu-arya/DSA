class Max_Heap:

    def __init__(self, size):
        self.size = size
        self.__li = [] #Array to store Elements
        self.heapSize = 0 #For Storing HeapSize

    def add(self, element):
        if self.heapSize == self.size:
            print('Max Heap Overflow')
            return

        self.__li.append(element)
        self.heapSize += 1

        # Heapify the array
        parent = self.heapSize // 2
        index = self.heapSize - 1

        while self.__li[parent] < self.__li[index] and index > 0:
            self.__li[parent], self.__li[index] = self.__li[index], self.__li[parent]
            index = parent
            parent = index // 2

    def pop(self):
        if self.heapSize < 1:
            print('Heap Underflow')
            return

        temp = self.__li[0]
        self.__li[0] = self.__li[self.heapSize-1]
        self.__li.pop()
        self.heapSize -= 1

        # Heapify the array
        index = 0
        while index < self.heapSize//2:
            left, right = 2*index, 2*index+1
            if self.__li[left] > self.__li[index] or self.__li[right] > self.__li[index]:
                if self.__li[left] > self.__li[right]:
                    self.__li[left], self.__li[index] = self.__li[index], self.__li[left]
                    index = left
                else:
                    self.__li[right], self.__li[index] = self.__li[index], self.__li[right]
                    index = right
            else:
                break

        return temp

    def print_heap(self):
        print(self.__li)

    def peek(self):
        return self.__li[0]

if __name__ == "__main__":
        maxHeap = Max_Heap(5)
        maxHeap.add(1)
        maxHeap.add(2)
        maxHeap.add(3)
        maxHeap.add(4)
        maxHeap.add(5)
        maxHeap.add(6)
        # [3,1,2]
        print(maxHeap.print_heap())
        print(maxHeap.pop())
        maxHeap.print_heap()
        print(maxHeap.pop())
        maxHeap.print_heap()
        print(maxHeap.pop())
        maxHeap.print_heap()
        print(maxHeap.pop())
        print(maxHeap.pop())
        print(maxHeap.pop())
        print(maxHeap.pop())
