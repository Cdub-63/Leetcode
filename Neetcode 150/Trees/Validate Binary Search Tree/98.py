class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, min_val, max_val):
            """
            This function takes in a node in a binary tree, and checks if it is a valid Binary Search Tree.
            It does this by checking if the node's value is within the valid range, and then recursing on the left and right subtrees.

            :param node: The current node being checked.
            :param min_val: The minimum valid value for this node.
            :param max_val: The maximum valid value for this node.
            :return: Whether the subtree rooted at this node is a valid Binary Search Tree.
            """
            if not node:
                # If the node is None, the tree is empty, so return True.
                return True

            if node.val <= min_val or node.val >= max_val:
                # If the node's value is outside the valid range, return False.
                return False

            # Recurse on the left subtree, with the minimum valid value being the same as the parent's, and the maximum valid value being the parent's value.
            # Recurse on the right subtree, with the minimum valid value being the parent's value, and the maximum valid value being the same as the parent's.
            return validate(node.left, min_val, node.val) and validate(node.right, node.val, max_val)
        
        return validate(root, float('-inf'), float('inf'))

# time complexity: O(n)
# space complexity: O(n)