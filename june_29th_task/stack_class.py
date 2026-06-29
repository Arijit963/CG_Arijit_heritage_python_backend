class Stack:

    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):

        if self.is_empty():
            raise IndexError("pop from an empty stack")

        return self._data.pop()

    def peek(self):

        if self.is_empty():
            raise IndexError("peek from an empty stack")

        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

    def __repr__(self):

        if self.is_empty():
            return "Stack: [EMPTY]"

        return f"Stack [bottom→top]: {self._data}"
    
    
#stack push
book_stack = Stack()

book_stack.push("Python Basics")
book_stack.push("Data Structures")
book_stack.push("Algorithms")
book_stack.push("System Design")
book_stack.push("Clean Code")

print(book_stack)
print(book_stack.size())
print(book_stack.peek())


#stack pop
print(book_stack.peek())

removed = book_stack.pop()
print(removed)

removed = book_stack.pop()
print(removed)

print(book_stack)

print(book_stack.is_empty())



