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


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()