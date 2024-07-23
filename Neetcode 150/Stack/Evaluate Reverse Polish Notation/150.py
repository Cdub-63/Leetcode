class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []  # Create an empty stack to store numbers

        for token in tokens:
            if token in {"+", "-", "*", "/"}:  # If the token is an operator
                num2 = stack.pop()  # Pop the top number off the stack
                num1 = stack.pop()  # Pop the next number off the stack
                if token == "+":  # If the operator is addition
                    result = num1 + num2  # Add the two numbers together
                elif token == "-":  # If the operator is subtraction
                    result = num1 - num2  # Subtract the second number from the first
                elif token == "*":  # If the operator is multiplication
                    result = num1 * num2  # Multiply the two numbers
                else:  # If the operator is division
                    result = int(num1 / num2)  # Divide the first number by the second
                stack.append(result)  # Push the result back onto the stack
            else:  # If the token is a number
                stack.append(int(token))  # Push the number onto the stack

        return stack[0]  # Return the top number on the stack, which is the result of evaluating the RPN expression

# Time Complexity: O(N)
# Space Complexity: O(N)