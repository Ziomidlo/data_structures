class Node:
    
    def __init__(self, data, n = None, p = None):
        self.data = data
        self.next_node = n
        self.prev_node = p

    def __str__(self):
        return ('(' + str(self.data) + ')')