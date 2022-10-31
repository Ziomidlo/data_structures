from Stack import Stack
from Queue import Queue

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.pop())
print(stack.peek())


queue = Queue()
print(queue.enqueue(19))
print(queue.enqueue(43))
print(queue.enqueue(45))
print(queue.dequeue())
print(queue.get_size())
