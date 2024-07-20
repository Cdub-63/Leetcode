class Solution:
    # Define a method to search for a target value within a sorted array.
    def search(self, nums: List[int], target: int) -> int:
        # Initialize two pointers, left and right, to the start and end of the array, respectively.
        left, right = 0, len(nums) - 1
        
        # Continue searching as long as left pointer does not surpass right pointer.
        while left <= right:
            # Calculate the middle index of the current segment of the array.
            mid = (left + right) // 2
            
            # If the middle element is the target, return its index.
            if nums[mid] == target:
                return mid
            
            # Check if the left half of the array is sorted.
            if nums[left] <= nums[mid]:
                # If the target is within the range of the sorted left half, adjust the right pointer to search within this half.
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                # Otherwise, adjust the left pointer to search in the right half.
                else:
                    left = mid + 1
            # If the left half is not sorted, then the right half must be sorted.
            else:
                # If the target is within the range of the sorted right half, adjust the left pointer to search within this half.
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                # Otherwise, adjust the right pointer to search in the left half.
                else:
                    right = mid - 1
        
        # If the target is not found in the array, return -1.
        return -1

# Time Complexity: O(log n), because we are performing binary search on the array
# Space Complexity: O(1)