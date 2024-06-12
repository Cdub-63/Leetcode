# Define a class for the solution
class Solution:
    # Define a method to remove all instances of a value from an array
    def removeElement(self, nums: List[int], val: int) -> int:
        # Initialize a counter for the number of elements not equal to the value
        k = 0
        # For each element in the array
        for i in range(len(nums)):
            # If the element is not equal to the value
            if nums[i] != val:
                # Copy it to the current position of the counter
                nums[k] = nums[i]
                # Increment the counter
                k += 1
        # Return the number of elements not equal to the value
        return k

# Define a class for the optimized solution
class Solution:
    # Define a method to remove all instances of a value from an array
    def removeElement(self, nums: List[int], val: int) -> int:
        # Initialize the length of the array and a counter
        n = len(nums)
        i = 0
        # While the counter is less than the length of the array
        while i < n:
            # If the current element is equal to the value
            if nums[i] == val:
                # Swap it with the last element of the array
                nums[i], nums[n - 1] = nums[n - 1], nums[i]
                # Decrement the length of the array
                n -= 1
            else:
                # Otherwise, increment the counter
                i += 1
        # Return the length of the array
        return n

# Time complexity: O(n), where n is the number of elements in the array
# Space complexity: O(1) since only a constant amount of extra space is used