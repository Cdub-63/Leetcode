class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers nums and a target integer, return an array of
        two integers that represents the indices of the two numbers that add up to
        the target. 

        Args:
        - nums (List[int]): The array of integers.
        - target (int): The target integer.

        Returns:
        - List[int]: A list of two integers representing the indices of the two
          numbers that add up to the target.
        """

        # Initialize an empty dictionary to store the difference between the target
        # and the current number as the key, and the index of the current number as
        # the value.
        d = {}

        # Iterate over the array of numbers.
        for i in range(len(nums)):
            # Calculate the difference between the target and the current number.
            n = target - nums[i]

            # If the difference is already in the dictionary, that means we have
            # found a pair of numbers that add up to the target.
            if n in d:
                # Return the indices of the two numbers.
                return [d[n], i]

            # Otherwise, add the current number to the dictionary with its index as
            # the value.
            d[nums[i]] = i

# time complexity: O(n)
# space complexity: O(n)