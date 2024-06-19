# Define a class for the solution
class Solution(object):
    # Define a method to guess a number between 1 and n
    def guessNumber(self, n):
        # Initialize pointers to the start (low) and end (high) of the search space
        low = 1
        high = n

        # While the search space is not empty
        while True:
            # Calculate the middle of the search space
            mid = low + (high - low) // 2
            # Call the guess function with the middle number
            myGuess = guess(mid)
            # If the guess function returns 1, the target is greater than the middle number
            if myGuess == 1:
                # Discard the left half of the search space
                low = mid + 1
            # If the guess function returns -1, the target is less than the middle number
            elif myGuess == -1:
                # Discard the right half of the search space
                high = mid - 1
            # If the guess function returns 0, the target is equal to the middle number
            else:
                # Return the middle number
                return mid

# time complexity: O(log(n)), where n is the range of numbers to guess
# space complexity: O(1)