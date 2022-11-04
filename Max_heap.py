class Max_heap:

    def __init__ (self, items=[]):
        super().__init__()
        self.heap = [0]
        for item in items:
            self.heap.append(item)
    
    def push(self, data):
        self.heap.append(data)

    def peek(self):
        if(self.heap[1]):
            return self.heap[1]
        else:
            return False

    def pop(self):
        if(self.heap > 2):
            self.__swap(max, len(self.heap) - 1)
            max = self.heap.pop()
    
    '''def __swap(self):
        size = len(self.heap)
        temp = self.heap[1]
        self.heap[1] = self.heap[size - 1]
        self.heap[size - 1] = temp
        return self.heap'''

    def __swap(self, i ,j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        
    def __bubble_down(self, index):
        left = index * 2
        right = index * 2 + 1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest = left
        if len(self.heap) > right and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != index:
            self.__swap(index,largest)
            self.__bubble_down(largest)


        


