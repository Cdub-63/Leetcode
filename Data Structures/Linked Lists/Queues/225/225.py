class MyStack:

    def __init__(self):
        self.q = deque()  # Use a deque to store the elements

    def push(self, x: int) -> None:
        self.q.append(x)  # Append the element to the end of the deque

    def pop(self) -> int:
        # Move all elements except the last one from the end of the deque to the beginning
        for _ in range(len(self.q) - 1):
            self.push(self.q.popleft())
        # Remove and return the last element from the deque
        return self.q.popleft()

    def top(self) -> int:
        return self.q[-1]  # Return the last element in the deque

    def empty(self) -> bool:
        return len(self.q) == 0  # Return True if the deque is empty, False otherwise

# Time complexity: O(n) for pop, O(1) for top and empty, where n is the number of elements in the stack
# Space complexity: O(n) for the deque, where n is the number of elements in the stack