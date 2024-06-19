class Solution(object):
    def firstBadVersion(self, n):
        # Initialize pointers to the start (l) and end (r) of the search space
        l, r = 1, n

        # While the search space is not empty
        while l < r:
            # Calculate the middle of the search space
            m = l + (r - l) // 2
            # Call the isBadVersion API with the middle version
            if isBadVersion(m):
                # If the middle version is bad, the first bad version is in the left half of the search space
                r = m
            else:
                # If the middle version is not bad, the first bad version is in the right half of the search space
                l = m + 1

        # The first bad version is the left pointer
        return l

# Time complexity: O(logN), where N is the number of versions.
# Space complexity: O(1)