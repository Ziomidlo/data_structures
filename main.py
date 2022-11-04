from Stack import Stack
from Queue import Queue
from Max_heap import Max_heap

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

heap = Max_heap()
heap.push(10)
heap.push(23)
heap.push(7)
heap.push(1)
heap.push(99)
print(heap)
print(heap.pop())
print(heap)
print(heap.peek())
