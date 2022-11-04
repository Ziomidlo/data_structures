class Max_heap:

    def __init__ (self, items=[]):
        super().__init__()
        self.heap = [0]
        for item in items:
            self.heap.append(item)
            self.__bubble_up(len(self.heap) - 1)
    
    def push(self, data):
        self.heap.append(data)
        self.__bubble_up(len(self.heap) - 1)

    def peek(self):
        if(self.heap[1]):
            return self.heap[1]
        else:
            return False

    def pop(self):
        max = 1
        last = len(self.heap) - 1
        if len(self.heap) > 2:
            self.__swap(max, last)
            deleted = self.heap.pop()
            self.__bubble_down(max)
        elif(len(self.heap) == 2):
            deleted = self.heap.pop()
        else:
            deleted = False
        return deleted

    
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

    def __bubble_up(self, index):
        parent = index // 2
        if index <= 1:
            return 
        elif self.heap[parent] < self.heap[index]:
            self.__swap(index, parent)
            self.__bubble_up(parent)

    def __str__(self):
        return str(self.heap)




        


