class Stack:
    def __init__(self):
        self.data = []
    
    def push(self, x):
        self.data.append(x)
        return "added: " , x
    
    def pop(self):
        if(len(self.data) >= 1):
            x = self.data.pop()
            return "removed: " , x
        else:
            return "There's an empty list!"

    def peek(self):
        if(len(self.data) >= 1):
            return self.data[-1]
        else:
            return "There's an empty list!"