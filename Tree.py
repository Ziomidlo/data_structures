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
        if self.left is not None and self.right is not None:
            return 1 + self.left.get_size() + self.right.get_size()
        elif self.left:
            return 1 + self.left.get_size()
        elif self.right:
            return 1 + self.right.get_size()
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

    def remove(self, data):

        #empty tree
        if self.data is None:
            return False
        
        #data is in root node
        elif self.left is None and self.right is None:
           self.data = None
        elif self.left and self.right is None:
            self.data = self.left 
        elif self.right and self.left is None:
            self.data = self.right
        elif self.left and self.right:
            delNodeParent = self.data
            delNode = self.right
            while delNode.left:
                delNodeParent = delNode
                delNode = delNode.left
            
            self.data = delNode.data
            if delNode.right:
                if delNodeParent.data > delNode.data:
                    delNodeParent.left = delNode.right
                elif delNodeParent.data < delNode.data:
                    delNodeParent.right = delNode.right
            else:
                if delNode.data < delNodeParent.data:
                    delNodeParent.left = None
                else:
                    delNodeParent.right = None


        # find node to remove
        parent = None
        while self.data != data:
            parent = self.data
            if self.data > data:
                self.data = self.left
            elif self.data < data:
                self.data = self.right

        #data not found
        if self.data is None or self.data != data:
            return False
        
        #remove-node has no children
        elif self.left is None and self.right is None:
            if parent.data > data:
                parent.left = None
            else:
                parent.right = None
            return True

        #remove-node has left child only
        elif self.left and self.right is None:
            if parent.data > data:
                parent.left = self.left
            else:
                parent.right = self.right
            return True
        
        #remove-node has right child only
        elif self.right and self.left is None:
            if parent.data > data:
                parent.left = self.left
            else:
                parent.right = self.right
            return True 
        
        #remove-node has left and right children
        else: 
            delNodeParent = self.data
            delNode = self.data.right
            while delNode.left:
                delNodeParent = delNode
                delNode = delNode.left
            
            self.data = delNode.data
            if delNode.right:
                if delNodeParent.data > delNode.data:
                    delNodeParent.left = delNode.right
                elif delNodeParent.data < delNode.data:
                    delNodeParent.right = delNode.right
                else:
                    if delNode.data < delNodeParent.data:
                        delNodeParent.left = None
                    else:
                        delNodeParent.right = None





                


        




        

