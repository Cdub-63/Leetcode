# Define a class for the solution
class Solution:
    # Define a method to calculate the number of ways to climb a staircase
    def climbStairs(self, n: int) -> int:
        # If there are 3 or fewer stairs, the number of ways to climb is the same as the number of stairs
        if n <= 3:
            return n
        # Initialize the number of ways to climb a staircase with 2 and 3 stairs
        n1, n2 = 2, 3

        # For each additional stair
        for i in range(4, n + 1):
            # The number of ways to climb is the sum of the number of ways to climb the previous two staircases
            n1, n2 = n2, n1 + n2
        # Return the number of ways to climb the staircase
        return n2
    
# Time complexity: O(n), where n is the number of stairs
# Space complexity: O(1) since only two variables are used to store the number of ways to climb the previous two staircases