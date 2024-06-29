class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Check if there are any duplicate elements in the given list.

        Args:
            nums (List[int]): The list of integers to be checked.
        
        Returns:
            bool: True if there are any duplicate elements in the list, False otherwise.
        
        Approach:
        - Convert the list of integers to a set. A set is a collection of unique elements.
        - If the length of the set (after converting the list to a set) is different from the
          length of the original list, then there are duplicate elements.
        - If the lengths are the same, it means all elements in the list are unique.
        """

        # Convert the list of integers to a set to remove duplicates
        nums_set = set(nums)

        # Check if the length of the set is different from the length of the original list
        if len(nums_set) != len(nums):
            return True  # There are duplicate elements
        else:
            return False  # No duplicate elements

# Time complexity: O(n), for number of elements in the list
# Space complexity: O(n), because we are using a set to store the list