class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):

        new_node = Node(data)

        new_node.next = self.head

        self.head = new_node

    def insert_at_end(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def insert_at_position(self, data, position):

        if position == 0:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)

        current = self.head

        for _ in range(position - 1):

            if current is None:
                raise IndexError("Position out of range")

            current = current.next

        new_node.next = current.next

        current.next = new_node

    def delete_by_value(self, data):

        if self.head is None:
            return

        if self.head.data == data:

            self.head = self.head.next
            return

        current = self.head

        while current.next:

            if current.next.data == data:

                current.next = current.next.next
                return

            current = current.next

    def traverse(self):

        elements = []

        current = self.head

        while current:

            elements.append(str(current.data))

            current = current.next

        return " -> ".join(elements) + " -> None"

    def search(self, data):

        current = self.head
        position = 0

        while current:

            if current.data == data:
                return position

            current = current.next
            position += 1

        return -1

    def length(self):

        count = 0

        current = self.head

        while current:

            count += 1

            current = current.next

        return count
    
ll = SinglyLinkedList()

ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)

ll.insert_at_beginning(5)

ll.insert_at_position(15, 2)

print(ll.traverse())

print(ll.length())

print(ll.search(20))

ll.delete_by_value(15)

print(ll.traverse())