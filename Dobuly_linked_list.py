from Node import Node 

class Doubly_linked_list:

    def __init__(self, r = None):
        self.root = r
        self.last = r
        self.size = 0
    
    def add(self, data):
        this_node = self.root
        if self.size == 0:
            new_node = Node(data)
            self.root = new_node
            self.last = self.root
        else:
            new_node = Node(data, self.root)
            this_node.prev_node = new_node
            self.root = new_node
        self.size += 1

    def find(self, data):
        this_node = self.root
        last_node = self.last
      
        while this_node is not None:
            if this_node.data == data or last_node.data == data:
                return data
            else:
                this_node= this_node.next_node
                last_node = last_node.prev_node
        return None

    def remove(self, data):
        this_node = self.root
        while this_node is not None:
            if this_node.data == data:
                if this_node.prev_node is None:
                    this_node.next_node.prev_node = None
                    self.root = this_node.next_node 
                elif this_node.next_node is None:
                    this_node.prev_node.next_node = None
                    self.last = this_node.prev_node 
                else:
                    this_node.prev_node.next_node = this_node.next_node
                    this_node.next_node.prev_node = this_node.prev_node
                self.size -= 1
                return True
            else:
                this_node = this_node.next_node
        return False

    def print_list(self):
        if self.root is None:
            return
        this_node = self.root
        print(this_node, end="->")
        while this_node.next_node is not None:
            this_node = this_node.next_node
            print(this_node, end="->")
        print()


    


         