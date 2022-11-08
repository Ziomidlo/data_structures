from Node import Node

class Circular_linked_list:

    def __init__(self, r = None):
        self.root = r
        self.size = 0
    
    def add(self, data):
        if self.size == 0:
            self.root = Node(data)
            self.root.next_node = self.root
        else:
            new_node = Node(data, self.root.next_node)
            self.root.next_node = new_node
        self.size += 1

    def find(self, data):
        this_node = self.root
        while True:
            if this_node.data == data:
                return data
            elif this_node.next_node == self.root:
                return False
            this_node = this_node.next_node

    def remove(self, data):
        this_node = self.root
        prev_node = None

        while True:
            if this_node.data == data:
                if prev_node is not None:
                    prev_node.next_node = this_node.next_node
                else:
                    while this_node.next_node != self.root:
                        this_node = this_node.next_node
                    this_node.next_node = self.root.next_node
                    self.root = self.root.next_node
                self.size -= 1
                return True
            elif this_node.next_node == self.root:
                return False
            prev_node = this_node
            this_node = this_node.next_node

    def print_list(self):
        if self.root is None:
            return
        this_node = self.root
        print(this_node, end='->')
        while this_node.next_node != self.root:
            this_node = this_node.next_node
            print(this_node, end='->')
        print()




            

        

