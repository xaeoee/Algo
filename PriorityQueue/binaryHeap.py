class MinHeap:
    def __init__(self, capacity):
        self.storage = [0] * capacity
        self.capacity = capacity
        self.size = 0

    def getParentIndex(self, index):
        return (index - 1) // 2
    
    def getLeftChildIndex(self, index):
        return 2 * index + 1

    def getRightChildIndex(self, index):
        return 2 * index + 2

    def hasParent(self, index):
        return self.getParentIndex(index) >= 0
    
    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < self.size

    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < self.size
    
    def parentValue(self, index):
        return self.storage[self.getParentIndex(index)]
    
    def leftChildValue(self, index):
        return self.storage[self.getLeftChildIndex(index)]

    def rightChildValue(self, index):
        return self.storage[self.getRightChildIndex(index)]

    def isFull(self):
        return self.size == self.capacity

    def swap(self, index1, index2):
        temp = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = temp

    def insert(self, data):
        if(self.isFull()):
            raise("Healp is Full")
        self.storage[self.size] = data
        self.size += 1
        self.heapifyUp(self.size - 1)
    
    def heapifyUp(self, index):
        # index = self.size - 1
        # while(self.hasParent(index) and self.parentValue(index) > self.storage[index]):
        #     self.swap(self.getParentIndex(index), index)
        #     index = self.getParentIndex(index)
        if (self.hasParent(index) and self.parentValue(index) > self.storage[index]):
            self.swap(self.getParentIndex(index), index)
            self.heapifyUp(self.getParentIndex(index))
heap = MinHeap(5)

heap.insert(10)
heap.insert(20)
heap.insert(5)

print(heap.storage[2])
