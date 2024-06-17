# Define a class for the solution
class Solution(object):
    # Define a method to sort an array of colors (0, 1, 2) in-place
    def sortColors(self, nums):
        # Initialize pointers to the left and right ends of the array
        l, r = 0, len(nums) - 1
        # Initialize a pointer to the current element
        i = 0

        # Define a helper function to swap two elements in the array
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        # While the current element is not past the right end of the array
        while i <= r:
            # If the current element is 0
            if nums[i] == 0:
                # Swap it with the element at the left pointer
                swap(i, l)
                # Move the left pointer and the current element pointer to the right
                l += 1
                i += 1
            # If the current element is 2
            elif nums[i] == 2:
                # Swap it with the element at the right pointer
                swap(i, r)
                # Move the right pointer to the left
                r -= 1
            # If the current element is 1
            else:
                # Move the current element pointer to the right
                i += 1