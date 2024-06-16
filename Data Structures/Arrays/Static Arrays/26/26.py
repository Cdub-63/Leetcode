# Define a class for the solution
class Solution:
    # Define a method to remove duplicates from a sorted array
    def removeDuplicates(self, nums: List[int]) -> int:
        # Initialize a pointer L to the first element
        L = 1
        
        # For each element in the array starting from the second
        for R in range(1, len(nums)):
            # If the current element is not equal to the previous
            if nums[R] != nums[R - 1]:
                # Copy it to the position of the pointer L
                nums[L] = nums[R]
                # Increment the pointer L
                L += 1
        # Return the position of the pointer L, which is the new length of the array
        return L
    
# Time complexity: O(n), where n is the number of elements in the array
# Space complexity: O(1) since only a constant amount of extra space is used