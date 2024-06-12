class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # Initialize an empty list to use as a stack for storing the scores
        score_stack = []
        
        # Iterate over each operation in the list of operations
        for o in operations:
            
            # If the operation is "+", and there are at least two scores in the stack
            if o == "+" and len(score_stack) >= 2:
                # Calculate the sum of the last two scores in the stack
                summed = score_stack[-2] + score_stack[-1]
                # Push the calculated sum onto the stack
                score_stack.append(summed)
                
            # If the operation is "D", and there is at least one score in the stack
            elif o == "D" and len(score_stack) >= 1:
                # Calculate the double of the last score in the stack
                doubled = score_stack[-1] * 2
                # Push the calculated double onto the stack
                score_stack.append(doubled)
                
            # If the operation is "C", and there is at least one score in the stack
            elif o == "C" and len(score_stack) >= 1:
                # Remove the last score from the stack
                score_stack.pop() 
                
            # If the operation is a number
            else: 
                # Convert the operation to an integer and push it onto the stack
                score_stack.append(int(o))

        # Return the sum of all the scores in the stack
        return sum(score_stack)

# Time complexity: O(n) where n is the number of operations
# Space complexity: O(n) where n is the number of operations