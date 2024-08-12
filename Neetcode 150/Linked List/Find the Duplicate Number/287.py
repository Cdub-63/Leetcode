class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

        There is only one repeated number in nums, return this repeated number.
        
        This function uses the two-pointer technique to find the repeated number.

        Args:
            nums (List[int]): The array of integers.

        Returns:
            int: The repeated number.
        """
        
        # Initialize two pointers, slow and fast, pointing to the first element of the array
        slow = nums[0]
        fast = nums[0]
        
        # Move the two pointers until they meet at the repeated number
        # Find the intersection point of the two pointers
        while True:
            # Move the slow pointer to the next element indicated by nums[slow]
            slow = nums[slow]
            # Move the fast pointer to the next element indicated by nums[nums[fast]]
            fast = nums[nums[fast]]
            # If the two pointers meet, they have found the repeated number
            if slow == fast:
                break
        
        # Initialize another pointer, called "pointer1", pointing to the first element of the array
        pointer1 = nums[0]
        # Move "pointer1" and "slow" together until they meet at the repeated number
        while pointer1 != slow:
            # Move "pointer1" to the next element indicated by nums[pointer1]
            pointer1 = nums[pointer1]
            # Move "slow" to the next element indicated by nums[slow]
        # Find the entrance to the cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        # Return the repeated number
        return slow

# Time Complexity: O(n)
# Space Complexity: O(1)