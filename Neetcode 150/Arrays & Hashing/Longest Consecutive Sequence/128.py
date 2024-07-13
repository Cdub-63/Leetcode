class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        This function finds the longest consecutive sequence in a list of numbers.
        It does this by creating a set from the list for constant time lookup.
        It then loops through each number in the set, checking if it is part of a sequence.
        If it is, it keeps incrementing a streak until it hits a number not in the set.
        The longest streak is then returned.
        """

        # If the list is empty, return 0
        if not nums:
            return 0

        # Convert the list into a set for O(1) lookup time
        num_set = set(nums)

        # Variable to store the longest consecutive sequence
        longest = 0

        # Loop through each number in the list
        for num in num_set:
            # If the number is not in the set, it is part of a sequence
            # This means the number to the left of it is not in the set, so it is the start of the sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                # keep incrementing the current streak until the number is not in the set
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                # update the longest consecutive sequence
                # This is done by checking if the current streak is longer than the longest streak so far
                longest = max(longest, current_streak)
            
        return longest

# Time complexity: O(n), where n is the number of elements in the list
# Space complexity: O(n), because we are using a set to store the list