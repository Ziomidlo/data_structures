from Node import Node

class Linked_list:
    def __init__(self, r = None):
        self.root = r
        self.size = 0
    
    def add(self, data):
        new_node = Node(data, self.root)
        self.root = new_node
        self.size += 1

    def find(self, data):
        this_node = self.root
        while this_node is not None:
            if this_node.data == data:
                return data
            else:
                this_node = this_node.next_node
        return None 




    
