class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # Initialize the maximum path sum result
        res = [root.val]

        # Define a helper function to compute the maximum path sum recursively
        def dfs(root):
            # Base case: empty tree
            if not root:
                return 0

            # Compute the maximum path sums in the left and right subtrees
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            # Compute the maximum path sum of the left subtree, without splitting
            # If the left subtree's path sum is negative, ignore it
            leftMax = max(leftMax, 0)

            # Compute the maximum path sum of the right subtree, without splitting
            # If the right subtree's path sum is negative, ignore it
            rightMax = max(rightMax, 0)

            # Compute the maximum path sum of the current tree, with splitting
            # This is the maximum path sum of the current tree, including the root node
            # and the maximum of the left subtree's path sum and the right subtree's path sum
            res[0] = max(res[0], root.val + leftMax + rightMax)

            # Return the maximum path sum of the current tree, without splitting
            # This is the maximum path sum of the current tree, excluding the root node
            # and the maximum of the left subtree's path sum and the right subtree's path sum
            return root.val + max(leftMax, rightMax)

        # Call the helper function to start the recursion
        dfs(root)

        # Return the maximum path sum result
        return res[0]

# Time Complexity: O(N), where N is the number of nodes in the tree
# Space Complexity: O(H), where H is the height of the tree