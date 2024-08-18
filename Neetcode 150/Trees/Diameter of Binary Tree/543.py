class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Calculate the diameter of a binary tree.

        The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
        This path may or may not pass through the root. The function uses a depth-first search (DFS) to
        recursively traverse the tree and calculate the diameter.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            int: The diameter of the binary tree.
        """
        # Initialize the diameter to 0. This will store the maximum diameter found so far.
        self.diameter = 0
        
        def dfs(node):
            """
            Recursively traverse the binary tree and calculate the diameter.

            Args:
                node (Optional[TreeNode]): The current node being traversed.

            Returns:
                int: The height of the subtree rooted at the current node.
            """
            # If the current node is None, return 0 as the height of the subtree.
            if not node:
                return 0
            
            # Recursively calculate the height of the left and right subtrees.
            left = dfs(node.left)
            right = dfs(node.right)
            
            # Update the diameter if the current diameter is greater than the previous diameter.
            # The diameter is the maximum height of the left and right subtrees plus the length of the path
            # between them to the root.
            self.diameter = max(self.diameter, left + right)
            
            # Return the maximum height of the left and right subtrees plus 1 for the current node.
            # This is the height of the subtree rooted at the current node.
            return max(left, right) + 1
        
        # Start the DFS traversal from the root node.
        dfs(root)
        
        # Return the calculated diameter.
        return self.diameter

# time complexity: O(N)
# space complexity: O(N)