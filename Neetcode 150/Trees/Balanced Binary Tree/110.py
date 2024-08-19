class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            """
            Perform a depth-first search of the binary tree starting at the given root.

            The search returns a tuple of two values. The first value is a boolean indicating
            whether the subtree rooted at the given root is balanced. The second value is the
            maximum depth of the subtree.

            Args:
                root (TreeNode): The root node of the subtree to search.

            Returns:
                tuple: A tuple containing a boolean indicating whether the subtree is balanced
                and the maximum depth of the subtree.
            """
            if not root:
                # If the subtree is empty, it is balanced and has a maximum depth of 0.
                return [True, 0]

            # Recursively search the left and right subtrees.
            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            # The subtree is balanced if both the left and right subtrees are balanced and
            # the depths of the left and right subtrees differ by at most 1.
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]

# Time Complexity: O(n)
# Space Complexity: O(h), where h is the height of the tree