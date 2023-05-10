class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def peek(self):
        if not self.is_empty():
            return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

myQueue = Queue()

print('is Empty: ', myQueue.is_empty())
myQueue.dequeue()
print('Peek: ', myQueue.peek())
print('Size: ', myQueue.size())

myQueue.enqueue(5)
print('Peek: ', myQueue.peek())
myQueue.enqueue(4)
print('Peek: ', myQueue.peek())
print('Size: ', myQueue.size())

myQueue.dequeue()
print('Peek: ', myQueue.peek())
print('is Empty: ', myQueue.is_empty())
print('Size: ', myQueue.size())