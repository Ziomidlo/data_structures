class Tree:

    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, data):
        if self.data == data:
            return False
        elif self.data > data:
            if self.left is not None:
                return self.left.insert(data)
            else:
                self.left = Tree(data)
                return True
        else:
            if self.right is not None:
                return self.right.insert(data)
            else:
                self.right = Tree(data)
                return True

    def find(self, data):
        if self.data == data:
            return data
        elif self.data > data:
            if self.left is not None:
                return self.left.find(data)
        elif self.data < data:
            if self.right is not None:
                return self.right.find(data)
        else:
            return False

    def get_size(self):
        size = 1
        if self.data is not None:
            if self.left is not None:
                size += 1
                return self.left.get_size()
            if self.right is not None:
                size += 1
                return self.right.get_size()
        else:
            return 1

    def preorder_traversal(self):
        if self is not None:
            print(self.data, end= ' ')
            if self.left is not None:
                self.left.preorder_traversal()
            if self.right is not None:
                self.right.preorder_traversal()
    
    def inorder_traversal(self):
        if self is not None:
            if self.left is not None:
                self.left.inorder_traversal()
            print(self.data, end=' ')
            if self.right is not None:
                self.right.inorder_traversal()


        




        

