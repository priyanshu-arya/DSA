class MinHeap:
    def __init__(self, size):
        self.__li = []
        self.heapSize = 0
        self.size = size

    def peak(self):
        return self.__li[0]

    def print_heap(self):
        print(self.__li)

    def add(self, element):
        if self.heapSize > self.size:
            print('Min Heap Overflow')
            return

        self.__li.append(element)
        self.heapSize += 1

        index, parent = self.heapSize - 1, self.heapSize // 2

        while self.__li[parent] > self.__li[index] and index > 0:
            self.__li[parent], self.__li[index] = self.__li[index], self.__li[parent]
            index = parent
            parent = index // 2

    def pop(self):
        if self.heapSize < 1:
            print("Min Heap Underflow")
            return

        temp = self.__li[0]
        self.__li[0] = self.__li[-1]
        self.__li.pop()
        self.heapSize -= 1

        index = 0
        while index < self.heapSize//2:
            left, right = 2*index, 2*index+1
            if self.__li[left] < self.__li[index] or self.__li[right] < self.__li[index]:
                if self.__li[left] < self.__li[right]:
                    self.__li[left], self.__li[index] = self.__li[index], self.__li[right]
                    index = left
                else:
                    self.__li[right], self.__li[index] = self.__li[index], self.__li[right]
                    index = right
            else:
                break

        return temp

if __name__ == "__main__":
        minHeap = MinHeap(5)
        minHeap.add(1)
        minHeap.add(2)
        minHeap.add(3)
        minHeap.add(4)
        minHeap.add(5)
        minHeap.add(6)
        # [3,1,2]
        print(minHeap.print_heap())
        print(minHeap.pop())
        minHeap.print_heap()
        print(minHeap.pop())
        print(minHeap.pop())
        minHeap.print_heap()
        print(minHeap.pop())
        print(minHeap.pop())
        minHeap.print_heap()
        print(minHeap.pop())
