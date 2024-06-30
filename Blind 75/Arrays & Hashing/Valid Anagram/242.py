class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

# Time complexity: O(n log n), because sorting is O(n log n)
# Space complexity: O(1), because no extra space is used