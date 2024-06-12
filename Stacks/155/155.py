# Define a class for a stack that supports retrieving the minimum element in constant time
class MinStack:
    # Define a method to initialize the stack
    def __init__(self):
        self.stack = []
        self.min_stack = []

    # Define a method to push an element onto the stack
    def push(self, x: int) -> None:
        self.stack.append(x)
        # If the min_stack is empty or the new element is smaller than the current minimum
        if not self.min_stack or x <= self.min_stack[-1]:
            # Push the new element onto the min_stack
            self.min_stack.append(x)

    # Define a method to remove the top element from the stack
    def pop(self) -> None:
        # If the top element is the current minimum
        if self.stack[-1] == self.min_stack[-1]:
            # Remove it from the min_stack
            self.min_stack.pop()
        # Remove the top element from the stack
        self.stack.pop()

    # Define a method to get the top element of the stack
    def top(self) -> int:
        return self.stack[-1]

    # Define a method to retrieve the minimum element in the stack
    def getMin(self) -> int:
        return self.min_stack[-1]

# Time complexity: O(1) for each operation
# Space complexity: O(n) where n is the number of elements in the stack