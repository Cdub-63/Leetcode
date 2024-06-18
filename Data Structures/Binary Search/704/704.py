class Solution(object):
    def search(self, nums, target):
        # Initialize pointers to the start (L) and end (R) of the array
        L, R = 0, len(nums) - 1

        # While the search space is not empty
        while L <= R:
            # Calculate the middle index of the search space
            mid = (L + R) // 2

            # If the target is greater than the middle element, discard the left half of the search space
            if target > nums[mid]:
                L = mid + 1
            # If the target is less than the middle element, discard the right half of the search space
            elif target < nums[mid]:
                R = mid - 1
            # If the target is equal to the middle element, return its index
            else:
                return mid
        # If the target is not found, return -1
        return -1

# The time complexity of binary search is O(log(n)) because it halves the search space at each step
# The space complexity of binary search is O(1) because it uses a constant amount of space