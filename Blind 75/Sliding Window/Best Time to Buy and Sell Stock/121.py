class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize a left pointer to the first day and a right pointer to the second day
        left = 0
        right = 1
        
        # Initialize a variable to keep track of the maximum profit
        max_profit = 0
        
        # Continue until the right pointer reaches the end of the array
        while right < len(prices):
            # If the price at the left pointer is less than the price at the right pointer,
            # calculate the potential profit by subtracting the price at the left pointer from the price at the right pointer
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                
                # Update the maximum profit if the current profit is greater than the previous maximum profit
                max_profit = max(max_profit, profit)
            else:
                # If the price at the right pointer is greater than or equal to the price at the left pointer,
                # move the left pointer to the right pointer to capture any potential future profits
                left = right
            
            # Move the right pointer to the next day
            right += 1
        
        # Return the maximum profit
        return max_profit

# Time Complexity: O(N), where N is the number of days
# Space Complexity: O(1)