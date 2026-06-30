from collections import deque

class Queue:

    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):

        if self.is_empty():
            raise IndexError("dequeue from empty queue")

        return self._data.popleft()

    def peek(self):

        if self.is_empty():
            raise IndexError("peek from empty queue")

        return self._data[0]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

    def __repr__(self):
        return f"Queue [front→rear]: {list(self._data)}"
    
    
    
# bank queue simulation
branch = Queue()

branch.enqueue("Priya")
branch.enqueue("Rajan")
branch.enqueue("Sunita")
branch.enqueue("Akash")

while not branch.is_empty():

    customer = branch.dequeue()

    print(customer)
    
