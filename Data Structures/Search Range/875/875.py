class Solution(object):
    def minEatingSpeed(self, piles, h):

        # Initialize the binary search boundaries. The minimum possible speed is 1 (eating at least one pile per hour),
        # and the maximum is the size of the largest pile.
        l, r = 1, max(piles)

        # Perform binary search
        while l < r:
            # Calculate the mid-point speed
            m = (l + r) // 2

            # Calculate the total hours needed to eat all bananas at the mid-point speed.
            # For each pile, we divide the pile size by the eating speed (pile // mid), rounding up to the nearest hour ((pile + mid - 1) // mid).
            # If the total hours exceeds h, the mid-point speed is too slow, so we set the left boundary to mid + 1.
            if sum((pile + m - 1) // m for pile in piles) > h:
                l = m + 1
            # If the total hours is less than or equal to h, the mid-point speed is fast enough, so we set the right boundary to mid.
            else:
                r = m

        # When the binary search is complete, left and right will converge to the minimum eating speed that allows us to eat all bananas within h hours.
        return l

# Time complexity: O(NlogM), where N is the number of piles, and M is the maximum size of a pile.
# Space complexity: O(1)