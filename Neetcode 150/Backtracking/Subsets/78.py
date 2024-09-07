class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Generate all possible subsets of the given list of numbers
        """
        res = []

        # Current subset we are constructing
        subset = []

        def dfs(i):
            """
            Depth-first search to construct all possible subsets
            """
            if i >= len(nums):
                # We have reached the end of the list, add the current subset
                res.append(subset.copy())
                return
            # Decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            # Decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res

# Time Complexity: O(2^N * N)
# Space Complexity: O(N)
