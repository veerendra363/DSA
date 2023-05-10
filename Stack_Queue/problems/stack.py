class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


myStack = Stack()

print('is Empty: ', myStack.is_empty())

print('Peek: ', myStack.peek())
myStack.pop()

myStack.push(5)
print('Peek: ', myStack.peek())

myStack.push(4)
print('Peek: ', myStack.peek())

print('Size: ', myStack.size())

myStack.pop()
print('Peek: ', myStack.peek())

print('is Empty: ', myStack.is_empty())