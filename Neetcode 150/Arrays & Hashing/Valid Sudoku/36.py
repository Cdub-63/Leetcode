class Solution:
    # This function checks if a Sudoku board is valid. 
    # It does this by checking each cell in the board.
    # If a cell is not empty, it checks if the number in that cell
    #   is already in the row, column, or box the cell is in.
    #   If it is, the board is not valid and the function returns False.
    # If a cell is empty, the function skips it.
    # If all cells are checked and no conflicts are found, the board is valid
    #   and the function returns True.
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize sets to store the numbers already in each row, column, and box
        # Sets are used because they have constant time complexity for lookups
        rows = [set() for _ in range(9)]  # One set for each row
        cols = [set() for _ in range(9)]  # One set for each column
        boxes = [set() for _ in range(9)]  # One set for each 3x3 box

        # Iterate over each row in the board
        for i in range(9):
            # Iterate over each cell in the row
            for j in range(9):
                # If the cell is empty, skip it
                if board[i][j] == ".":
                    continue
                
                # Get the number in the cell
                num = board[i][j]

                # Calculate the index of the 3x3 box the cell is in
                box_index = (i // 3) * 3 + j // 3

                # Check if the number in the cell is already in the row, column, or box
                if num in rows[i] or num in cols[j] or num in boxes[box_index]:
                    # If it is, the board is not valid and the function returns False
                    return False
                
                # Add the number to the sets for the row, column, and box
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_index].add(num)

        # If all cells are checked and no conflicts are found, the board is valid
        #   and the function returns True
        return True

# Time Complexity: O(1), because we only iterate over the board once
# Space Complexity: O(1), because we only store the sets in the program