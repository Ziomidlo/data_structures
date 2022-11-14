from Stack import Stack
from Queue import Queue
from Max_heap import Max_heap
from Linked_list import Linked_list
from Circular_linked_list import Circular_linked_list
from Dobuly_linked_list import Doubly_linked_list
from Tree import Tree

'''stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.pop())
print(stack.peek())'''


'''queue = Queue()
print(queue.enqueue(19))
print(queue.enqueue(43))
print(queue.enqueue(45))
print(queue.enqueue(7))
print(queue.enqueue(23))
print(queue.get_size())
print(queue.get_queue())
print(queue.swap())
print(queue.get_queue())
'''

'''heap = Max_heap()
heap.push(10)
heap.push(23)
heap.push(7)
heap.push(1)
heap.push(99)
print(heap)
print(heap.pop())
print(heap)
print(heap.peek())'''

'''myList = Linked_list()
myList.add(5)
myList.add(7)
myList.add(11)
myList.add(6)
myList.add(49)
myList.print_list()

print("size= " + str(myList.size))
myList.remove(11)
myList.print_list()
print("size= " + str(myList.size))
print (myList.find(5))
print("root= " + str(myList.root))'''

'''cll = Circular_linked_list()
cll.add(5)
cll.add(7)
cll.add(11)
cll.add(6)
cll.add(49)
cll.print_list()

print("size= " + str(cll.size))
cll.remove(11)
print("size= " + str(cll.size))
print(cll.find(5))
print("root= " + str(cll.root))'''


'''dll = Doubly_linked_list()
dll.add(5)
dll.add(7)
dll.add(11)
dll.add(6)
dll.add(49)
dll.print_list()

print("size= " +  str(dll.size))
dll.remove(11)
dll.print_list()
print("size= " + str(dll.size))
print(dll.find(5))
print(dll.last.prev_node)
'''

tree = Tree(7)
tree.insert(9)
for i in [5, 12, 6, 4, 28, 50, 8, 11]:
    tree.insert(i)
print(tree.find(7))
print(tree.find(99))
print('\n', tree.get_size())
tree.preorder_traversal()
print()
tree.inorder_traversal()