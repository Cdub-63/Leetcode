# Implementing a stack is trivial using a dynamic array
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, n):
        self.stack.append(n)

    def pop(self):
        return self.stack.pop()

# Time complexity: O(1) for all operations
# Space complexity: O(n) where n is the number of elements in the stack