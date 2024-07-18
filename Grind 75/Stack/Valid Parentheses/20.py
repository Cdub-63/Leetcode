class Solution:
    def isValid(self, s: str) -> bool:
        """
        This function checks if a string of parentheses is valid.
        A string of parentheses is valid if:
            - Open brackets must be closed by the same type of brackets.
            - Open brackets must be closed in the correct order.
            - Every close bracket has a corresponding open bracket of the same type.

        The function uses a stack to keep track of the open brackets.
        It iterates over each character in the string.
        If the character is an open bracket, it is pushed onto the stack.
        If the character is a close bracket, it checks if the stack is empty or if the top of the stack
        does not match the corresponding open bracket. If either of these conditions is true, the function
        returns False.
        If the character is not a bracket, it is simply pushed onto the stack.
        At the end of the function, if the stack is empty, the string is valid. Otherwise, it is not.
        """
        # Define a map of closing to opening parentheses
        Map = {")": "(", "]": "[", "}": "{"}

        stack = []

        # Iterate over the characters in the string
        for char in s:
            # If the character is an opening parenthesis
            if char not in Map:
                # Push it onto the stack
                stack.append(char)
                continue
            # If the stack is empty or the top of the stack is not the corresponding opening parenthesis
            elif not stack or Map[char] != stack.pop():
                # The string is not valid
                return False

        # If the stack is empty, the string is valid
        return not stack

# Time complexity: O(n)
# Space complexity: O(n)