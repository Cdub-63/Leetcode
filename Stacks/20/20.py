# Define a class for the solution
class Solution:
    # Define a method to check if a string of parentheses is valid
    def isValid(self, s: str) -> bool:
        # Define a map of closing to opening parentheses
        Map = {")": "(", "]": "[", "}": "{"}
        # Initialize an empty stack
        stack = []

        # Iterate over the characters in the string
        for c in s:
            # If the character is an opening parenthesis
            if c not in Map:
                # Push it onto the stack
                stack.append(c)
                continue
            # If the stack is empty or the top of the stack is not the corresponding opening parenthesis
            if not stack or stack[-1] != Map[c]:
                # The string is not valid
                return False
            # Pop the top of the stack
            stack.pop()

        # If the stack is empty, the string is valid
        return not stack

# Time complexity: O(n), where n is the length of the input string
# Space complexity: O(n), where n is the length of the input string