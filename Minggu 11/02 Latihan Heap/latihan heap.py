import sys
  
class MaxHeap:
    def __init__(self, maxsize):          
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = sys.maxsize
        self.FRONT = 1
  
    def parent(self, index):
        return index // 2
  
    def leftChild(self, index):
        return 2 * index

    def rightChild(self, index):
        return (2 * index) + 1
  
    def isLeaf(self, index): #mengecek apakah memiliki child atau tidak bernilai true jika tidak memiliki child
        if index >= (self.size//2) and index <= self.size:
            return True
        return False

    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = (self.Heap[spos], self.Heap[fpos])

    def maxHeapify(self, index):
        if not self.isLeaf(index):
            if (self.Heap[index] < self.Heap[self.leftChild(index)] and 
            self.Heap[index] < self.Heap[self.rightChild(index)]):
                if (self.Heap[self.leftChild(index)] > self.Heap[self.rightChild(index)]):
                    self.swap(index, self.leftChild(index))
                    self.maxHeapify(self.leftChild(index))
                else:
                    self.swap(index, self.rightChild(index))
                    self.maxHeapify(self.rightChild(index))
  
    def insert(self, element):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = element

        current = self.size

        while (self.Heap[current] > self.Heap[self.parent(current)]):
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def Print(self):
        for i in range(1, (self.size // 2) + 1):
            print(" PARENT : " + str(self.Heap[i]) + 
                  " LEFT CHILD : " + str(self.Heap[2 * i]) + 
                  " RIGHT CHILD : " + str(self.Heap[2 * i + 1]))
        
      
    def extractMax(self): #node root
        nilai_max = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.maxHeapify(self.FRONT)
              
        return print(nilai_max)

class MinHeap: #nilai paling atas nilai min
 
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0]*(self.maxsize + 1)
        self.Heap[0] = -1 * sys.maxsize
        self.FRONT = 1

    def parent(self, index):
        return index//2
 
    def leftChild(self, index):
        return 2 * index
 
    def rightChild(self, index):
        return (2 * index) + 1
 
    def isLeaf(self, index):
        if index >= (self.size//2) and index <= self.size:
            return True
        return False
 
    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    def minHeapify(self, index):
        if not self.isLeaf(index):
            if (self.Heap[index] > self.Heap[self.leftChild(index)] or
               self.Heap[index] > self.Heap[self.rightChild(index)]):
                if self.Heap[self.leftChild(index)] < self.Heap[self.rightChild(index)]:
                    self.swap(index, self.leftChild(index))
                    self.minHeapify(self.leftChild(index))
                else:
                    self.swap(index, self.rightChild(index))
                    self.minHeapify(self.rightChild(index))
 
    def insert(self, element):
        if self.size >= self.maxsize :
            return
        self.size+= 1
        self.Heap[self.size] = element

        current = self.size
 
        while self.Heap[current] < self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)
 
    def Print(self):
        for i in range(1, (self.size // 2) + 1):
            print(" PARENT : " + str(self.Heap[i]) + 
                  " LEFT CHILD : " + str(self.Heap[2 * i]) + 
                  " RIGHT CHILD : " + str(self.Heap[2 * i + 1]))
 
    def minHeap(self):
 
        for index in range(self.size//2, 0, -1):
            self.minHeapify(index)
 
    def remove(self):
 
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size-= 1
        self.minHeapify(self.FRONT)
        return popped

########################### DRIVER PROGRAM ###################################

#Buat MaxHeap
# maksimal = MaxHeap(5)

#insert MaxHeap
# maksimal.insert(4)
# maksimal.insert(2)
# maksimal.insert(5)
# maksimal.insert(3)
# maksimal.insert(1)

#         5
#     3        4
#  2     1

#Print MaxHeap
# maksimal.Print()

#Buat MinHeap
Minimal = MinHeap(5)

#insert Minheap
Minimal.insert(4)
Minimal.insert(2)
Minimal.insert(5)
Minimal.insert(3)
Minimal.insert(1)

#Print MaxHeap
Minimal.Print()
#         1
#      2     5
#   4     3 
