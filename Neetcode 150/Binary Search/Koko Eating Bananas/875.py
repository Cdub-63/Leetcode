class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        This function calculates the minimum speed at which Koko can eat all the bananas within h hours.
        It uses a binary search approach to find the minimum speed.
        """
        # Set the left and right boundaries of the binary search.
        # The left boundary is 1, the minimum possible speed.
        # The right boundary is the maximum size of a pile, which is the maximum speed.
        left, right = 1, max(piles)

        # Perform binary search
        while left < right:
            # Calculate the mid-point speed
            middle = (left + right) // 2

            # Calculate the total hours needed to eat all bananas at the mid-point speed.
            # For each pile, we divide the pile size by the eating speed (pile // middle), rounding up to the nearest hour ((pile + middle - 1) // middle).
            # If the total hours exceeds h, the mid-point speed is too slow, so we set the left boundary to mid + 1.
            # If the total hours is less than or equal to h, the mid-point speed is fast enough, so we set the right boundary to mid.
            if sum((pile + middle - 1) // middle for pile in piles) > h:
                left = middle + 1
            else:
                right = middle

        # When the binary search is complete, left and right will converge to the minimum eating speed that allows us to eat all the bananas within h hours.
        return left

# Time complexity: O(NlogM), where N is the number of piles, and M is the maximum size of a pile.
# Space complexity: O(1)