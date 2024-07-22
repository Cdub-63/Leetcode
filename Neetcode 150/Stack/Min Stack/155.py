
class MinStack:
    def __init__(self):
        # Initialize an empty stack to store all elements
        self.stack = []
        
        # Initialize an empty stack to keep track of the minimum element at each step
        self.min_stack = []
            
    def push(self, val: int) -> None:
        """
        Pushes a new element onto the stack. If the stack is empty or the new element
        is smaller than the current minimum element, update the minimum stack as well.
        """
        # Add the new element to the stack
        self.stack.append(val)

        # Check if the stack is empty or the new element is smaller than the current
        # minimum element
        if not self.min_stack or val <= self.min_stack[-1]:
            # If so, add the new element to the minimum stack as well
            self.min_stack.append(val)

    def pop(self) -> None:
        """
        Pops the top element from the stack. If the popped element is the current
        minimum element, remove it from the minimum stack as well.
        """
        # If the top element is the current minimum
        if self.stack[-1] == self.min_stack[-1]:
            # Remove it from the min_stack
            self.min_stack.pop()
        # Remove the top element from the stack
        self.stack.pop()

    def top(self) -> int:
        """
        Returns the top element of the stack. This is the most recently added element
        to the stack.

        :return: The top element of the stack
        """
        # The top element is just the last element in the stack
        return self.stack[-1]

    def getMin(self) -> int:
            """
            Returns the minimum element in the stack, which is tracked by the min_stack.
            The minimum element is always stored at the end of the min_stack.

            :return: The minimum element in the stack
            """
            return self.min_stack[-1]

# Time complexity: O(1) for each operation
# Space complexity: O(n) where n is the number of elements in the stack