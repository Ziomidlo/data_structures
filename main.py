from Stack import Stack
from Queue import Queue
from Max_heap import Max_heap
from Linked_list import Linked_list
from Circular_linked_list import Circular_linked_list

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

cll = Circular_linked_list()
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
print("root= " + str(cll.root))

