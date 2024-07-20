class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        This function finds the minimum element in a rotated sorted array.
        The array is rotated such that the minimum element is not at the beginning.
        This function uses a binary search approach to find the minimum element.
        """
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            # If the middle element is greater than the rightmost element,
            # the minimum is in the right half
            # This is because the array is sorted in ascending order, so
            # if the middle element is greater than the rightmost element,
            # the minimum is in the right half.
            if nums[mid] > nums[right]:
                left = mid + 1
            # If the middle element is less than or equal to the rightmost element,
            # the minimum is in the left half or it's the middle element itself
            # This is because the array is rotated, so the middle element
            # could be the minimum element or it could be in the left half.
            else:
                right = mid
        
        # When left == right, we've found the minimum element
        # This is because the array is sorted in ascending order and
        # the array is rotated, so we've found the leftmost element
        # that is less than or equal to all the other elements.
        return nums[left]

# Time Complexity: O(log n), because we are using binary search
# Space Complexity: O(1), because we are using constant space