# Define a class for the solution
class Solution(object):
    # Define a method to sort an array of colors (0, 1, 2) in-place
    def sortColors(self, nums):
        # Initialize a list to count the occurrences of each color
        count = [0, 0, 0]
        # Iterate over the array
        for num in nums:
            # Increment the count for the current color
            count[num] += 1
        # Initialize a pointer to the start of the array
        i = 0
        # Iterate over the count list
        for j in range(len(count)):
            # While there are still occurrences of the current color
            while count[j] > 0:
                # Set the current element of the array to the current color
                nums[i] = j
                # Move the pointer to the next element of the array
                i += 1
                # Decrement the count for the current color
                count[j] -= 1