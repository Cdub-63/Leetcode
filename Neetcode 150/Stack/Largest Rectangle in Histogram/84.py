class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Given an array of integers representing the heights of bars in a histogram,
        return the area of the largest rectangle that can be created by stacking bars.
        """
        # Initialize an empty list to store indices and heights of bars
        stack = []
        # Initialize a variable to store the maximum area of a rectangle
        max_area = 0
        # Add a 0 at the end of the heights list to make the last bar a boundary
        heights.append(0)

        # Loop through each bar in the histogram
        for i, h in enumerate(heights):
            # Initialize the start index of the current bar
            start = i
            # While there are bars on the stack and the current bar is taller than the top bar
            while stack and stack[-1][1] > h:
                # Pop the top bar off the stack
                index, height = stack.pop()
                # Calculate the area of the rectangle formed by the top bar and the current bar
                # by multiplying the height of the bar by the distance between the start index and the current index
                area = height * (i - index)
                # Update the maximum area if the current area is greater
                max_area = max(max_area, area)
                # Set the start index to the index of the popped bar
                max_area = max(max_area, height * (i - index))
                start = index
            # Add the current bar to the stack along with its index
            stack.append((start, h))

        # Return the maximum area of a rectangle that can be created by stacking bars
        return max_area

#time complexity: O(n)
#space complexity: O(n)