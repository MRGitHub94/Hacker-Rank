# Balance the symbols 
# Return True if the string is balanced

class Stack:
    def __init__(self):
        self._stack = []

    def push(self, item):
        self._stack.append(item)

    def pop(self):
        self._stack.pop()

    def is_empty(self):
        """Returns true if the queue is empty"""
        return not self._stack


def is_balanced_symbols(string):
    # implement a queue to push or pop off characters that are keys or values
    result = Stack()
    push, pops = "{[(", "}])"
    for char in string:
        if char in push:
            result.push(char)
        if char in pops:
            if result.is_empty():
                return False
            top = result.pop()
            if push[char] != top:
                return False

    return True

print is_balanced_symbols("(())")
# >>> True
print is_balanced_symbols("(([]))")
