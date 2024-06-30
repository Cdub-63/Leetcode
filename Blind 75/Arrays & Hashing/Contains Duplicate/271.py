class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

# Time complexity: O(n), for number of elements in the list
# Space complexity: O(n), because we are using a set to store the list