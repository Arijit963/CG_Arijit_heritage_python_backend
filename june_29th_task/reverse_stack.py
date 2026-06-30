
from stack_class import Stack


def reverse_string(s):

    stack = Stack()

    for char in s:
        stack.push(char)

    result = ""

    while not stack.is_empty():
        result += stack.pop()

    return result


print(reverse_string("Hello"))