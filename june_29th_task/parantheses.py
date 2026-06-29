from stack_class import Stack

def is_balanced(expr):

    stack = Stack()

    opening = set("({[")

    match = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    for ch in expr:

        if ch in opening:

            stack.push(ch)

        elif ch in match:

            if stack.is_empty():
                return False

            top = stack.pop()

            if top != match[ch]:
                return False

    return stack.is_empty()


print(is_balanced("({[]})"))