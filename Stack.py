class Stack:
    def __init__(self):
        self.data = []
    
    def push(self, x):
        self.data.append(x)
        return x
    
    def pop(self):
        x = self.data.pop()
        return x

    def peek(self):
        return self.data[-1]