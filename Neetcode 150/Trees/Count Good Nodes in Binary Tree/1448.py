class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxVal):
            """
            This is a recursive depth-first search function, which traverses the binary tree
            and returns the number of good nodes in the tree.

            :param node: The current node being traversed.
            :param maxVal: The maximum value of the current path from the root to the current node.
            :return: The number of good nodes in the subtree rooted at the current node.
            """

            # If the current node is None, return 0 as the number of good nodes.
            if not node:
                return 0

            # Initialize the number of good nodes to 0.
            res = 0

            # If the current node's value is greater than or equal to the maximum value of the path
            # so far, it is a good node. Increment the number of good nodes.
            if node.val >= maxVal:
                res += 1

            # Update the maximum value of the path so far.
            maxVal = max(maxVal, node.val)

            # Recursively traverse the left and right subtrees and add the number of good nodes
            # in the subtrees to the total number of good nodes.
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)

            # Return the total number of good nodes in the subtree.
            return res

        return dfs(root, root.val)

# Time Complexity: O(N)
# Space Complexity: O(H)