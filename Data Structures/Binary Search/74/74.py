# Define a class for the solution
class Solution:
    # Define a method to search for a target value in a matrix
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Get the number of rows and columns in the matrix
        ROWS, COLS = len(matrix), len(matrix[0])

        # Initialize pointers to the top and bottom rows
        top, bot = 0, ROWS - 1
        # While the search space is not empty
        while top <= bot:
            # Calculate the middle row of the search space
            row = (top + bot) // 2
            # If the target is greater than the last element of the middle row, discard the top half of the search space
            if target > matrix[row][-1]:
                top = row + 1
            # If the target is less than the first element of the middle row, discard the bottom half of the search space
            elif target < matrix[row][0]:
                bot = row - 1
            # If the target is within the range of the middle row, break the loop
            else:
                break

        # If the target is not within the range of any row, return False
        if not (top <= bot):
            return False
        # Calculate the middle row of the search space
        row = (top + bot) // 2
        # Initialize pointers to the left and right columns
        l, r = 0, COLS - 1
        # While the search space is not empty
        while l <= r:
            # Calculate the middle column of the search space
            m = (l + r) // 2
            # If the target is greater than the middle element of the middle row, discard the left half of the search space
            if target > matrix[row][m]:
                l = m + 1
            # If the target is less than the middle element of the middle row, discard the right half of the search space
            elif target < matrix[row][m]:
                r = m - 1
            # If the target is equal to the middle element of the middle row, return True
            else:
                return True
        # If the target is not found, return False
        return False
    
# Time complexity: O(log(m) + log(n)), where m is the number of rows and n is the number of columns in the matrix
# Space complexity: O(1) because it uses a constant amount of space