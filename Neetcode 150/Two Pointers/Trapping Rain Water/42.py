class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Given an array of non-negative integers representing the heights of bars in a bar chart, 
        return the maximum amount of water that can be trapped in the chart by two bars of height y1 and y2.
        The water area is the minimum of y1 and y2 multiplied by the distance between them.
        """
        if not height:
            return 0

        # Initialize two pointers at the start and end of the array
        left, right = 0, len(height) - 1

        # Initialize the maximum heights of the left and right pointers
        left_max, right_max = 0, 0

        # Initialize the water area
        water = 0

        # Iterate through the array until the two pointers meet
        while left < right:
            # Check if the left pointer's height is less than the right pointer's height
            if height[left] < height[right]:
                # Check if the left pointer's height is greater than or equal to the maximum height of the left pointer
                if height[left] >= left_max:
                    # Update the maximum height of the left pointer
                    left_max = height[left]
                else:
                    # Calculate the water area of the current iteration
                    water += left_max - height[left]
                # Move the left pointer to the right
                left += 1
            else:
                # Check if the right pointer's height is greater than or equal to the maximum height of the right pointer
                if height[right] >= right_max:
                    # Update the maximum height of the right pointer
                    right_max = height[right]
                else:
                    # Calculate the water area of the current iteration
                    water += right_max - height[right]
                # Move the right pointer to the left
                right -= 1

        # Return the total water area
        return water

# Time Complexity: O(n)
# Space Complexity: O(1)