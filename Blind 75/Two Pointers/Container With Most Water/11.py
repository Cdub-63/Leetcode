class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Initialize two pointers, one at the start of the array and one at the end
        left = 0
        right = len(height) - 1
        # Initialize a variable to keep track of the maximum water that can be contained in any container
        max_water = 0

        # Iterate until the pointers meet
        while left < right:
            # Calculate the width of the container
            width = right - left
            # Take the minimum height of the two pointers as the height of the container
            container_height = min(height[left], height[right])
            # Calculate the amount of water that can be contained in the container
            water = width * container_height
            # Update the maximum water if the current container can hold more water
            max_water = max(max_water, water)

            # If the height of the left pointer is less than the height of the right pointer,
            # move the left pointer to the right
            if height[left] < height[right]:
                left += 1
            # Otherwise, move the right pointer to the left
            else:
                right -= 1

        # Return the maximum amount of water that can be contained in any container
        return max_water

# Time Complexity: O(n), where n is the length of the array
# Space Complexity: O(1)