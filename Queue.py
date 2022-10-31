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
            return print("The queue has only: ", size, " element")
        elif (size == 0):
            return print("The queue has no elements!")
        else:
            return print("The queue has: ", size, " elements")
            



        