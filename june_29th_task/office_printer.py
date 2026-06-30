from collections import deque

class OfficePrinter:

    def __init__(self):

        self.queue = deque()

    def submit(self, document):

        self.queue.append(document)

    def print_next(self):

        if self.queue:

            return self.queue.popleft()


printer = OfficePrinter()

printer.submit("Report")
printer.submit("Invoice")

print(printer.print_next())