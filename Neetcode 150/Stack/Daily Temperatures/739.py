class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Get the length of the temperatures list
        n = len(temperatures)
        
        # Create an empty list to store the answer
        answer = [0] * n
        
        # Create an empty list to act as a stack
        stack = []
        
        # Iterate over each day in the temperatures list
        for i in range(n):
            # While there are still days on the stack and the current day's
            # temperature is greater than the temperature of the day at the top
            # of the stack, pop the top day from the stack. This means that the
            # current day is warmer than the previous day.
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # Get the previous day that was popped from the stack
                prev_day = stack.pop()
                
                # Calculate the number of days until the previous day was warmer
                # by subtracting the indices of the current day and the previous
                # day.
                answer[prev_day] = i - prev_day
            
            # Add the index of the current day to the stack. This means that the
            # current day is colder than the previous day.
            stack.append(i)
        
        # Return the list of answer
        return answer

# Time Complexity: O(n), where n is the number of days. We go through each day once, and each day is added and removed from the stack at most once.
# Space Complexity: O(n). In the worst case (when temperatures are in decreasing order), our stack could contain all n days.