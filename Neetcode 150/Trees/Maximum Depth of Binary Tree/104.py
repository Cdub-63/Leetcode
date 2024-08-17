class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # We are trying to find the maximum depth of a binary tree.
        # The maximum depth is the number of nodes along the longest path from the root
        # node down to the farthest leaf node.

        # If the tree is empty, its depth is 0.
        if not root:
            return 0

        # To find the maximum depth of a node, we need to find the maximum depths of its
        # left and right subtrees. We do this by recursively calling the maxDepth method.
        # The depth of a node is the max of its left and right depths, plus 1 for the node itself.

        # Calculate the depth of the left subtree.
        left_depth = self.maxDepth(root.left)

        # Calculate the depth of the right subtree.
        right_depth = self.maxDepth(root.right)

        # The depth of the current node is the maximum of its left and right depths, plus 1.
        # This is the maximum depth of the subtree rooted at this node.
        return max(left_depth, right_depth) + 1

# time complexity: O(n)
# space complexity: O(n)