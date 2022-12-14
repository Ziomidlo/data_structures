class Queue: 
    def __init__(self):
        self.data = []

    def enqueue(self, val):
        self.data.append(val)
        return val

    def dequeue(self):
        if(len(self.data) >= 1):
            val = self.data.pop(0) 
            return "removed", val
        else:
            return "There is an empty queue!"
    
    def get_size(self):
        size = len(self.data)
        if(size == 1):
            print("The queue has only: ", size, " element")
        elif (size == 0):
            print("The queue has no elements!")
        else:
            print("The queue has: ", size, " elements")

    def get_queue(self):
        if(len(self.data) > 0):
            for i in self.data:
                print(i)
        else:
            return "queue is empty!"
        
    def swap(self):
        size = len(self.data)
        temp = self.data[1]
        self.data[1] = self.data[size - 1]
        self.data[size - 1] = temp       
        return self.data


        