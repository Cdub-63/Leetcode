class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # This list will store all the valid combinations of 'n' pairs of parentheses.
        result = []

        # This recursive backtracking algorithm generates all possible combinations
        # of 'n' pairs of parentheses.
        def backtrack(s, left, right):
            # If the current string 's' has length equal to 2 * n, it means we have
            # generated a valid combination of parentheses. We append it to the
            # result list and return.
            if len(s) == 2 * n:
                result.append(s)  # Append the valid combination to the result list
                return
            
            # If the number of left parentheses is less than 'n', we can add a
            # left parenthesis to the current string. We increment the left
            # parentheses count and recursively call the backtrack function.
            if left < n:
                backtrack(s + "(", left + 1, right)  # Recursively call with an additional left parenthesis
            
            # If the number of right parentheses is less than the number of left
            # parentheses, we can add a right parenthesis to the current string.
            # We increment the right parentheses count and recursively call the
            # backtrack function.
            if right < left:
                backtrack(s + ")", left, right + 1)  # Recursively call with an additional right parenthesis

        # Start the backtracking process with an empty string, 0 left parentheses,
        # and 0 right parentheses.
        backtrack("", 0, 0)
        
        # Return the list of valid combinations of parentheses.
        return result

# time complexity: O(4^n / √n), because for each position, we have at most two choices, and we're making 2n choices in total.
# space complexity: O(n)