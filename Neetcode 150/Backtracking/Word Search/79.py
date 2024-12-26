class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return False
        
        rows, cols = len(board), len(board[0])
        
        # Optimization 1: Check if all characters in word exist in board
        board_chars = set(char for row in board for char in row)
        if any(char not in board_chars for char in word):
            return False
        
        # Optimization 2: Check if we have enough characters
        from collections import Counter
        board_counter = Counter(char for row in board for char in row)
        word_counter = Counter(word)
        if any(count > board_counter[char] for char, count in word_counter.items()):
            return False
        
        def dfs(row: int, col: int, index: int) -> bool:
            # Base case: if we've matched all characters, return True
            if index == len(word):
                return True
            
            # Check bounds and character match
            if (row < 0 or row >= rows or 
                col < 0 or col >= cols or 
                board[row][col] != word[index]):
                return False
            
            # Mark current cell as visited by changing it temporarily
            temp = board[row][col]
            board[row][col] = '#'
            
            # Try all four directions
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if dfs(new_row, new_col, index + 1):
                    return True
            
            # Restore the cell
            board[row][col] = temp
            return False
        
        # Start search from each cell in the grid
        # Optimization 3: Start with cells that match the first character
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        
        return False

#Time complexity: O(m∗4n)
#Space complexity: O(n)