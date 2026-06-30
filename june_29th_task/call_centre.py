from collections import deque

calls = deque()

calls.append("Customer 1")
calls.append("Customer 2")
calls.append("Customer 3")

while calls:

    print("Serving:", calls.popleft())