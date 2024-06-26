# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Perform an inorder traversal of a binary tree starting from the given root node.

        Parameters:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            List[int]: A list containing the values of the nodes in inorder traversal.
        """
        result = []

        def helper(root):
            if not root:
                return
            helper(root.left)
            result.append(root.val)
            helper(root.right)
        
        helper(root)
        return result

# Time Complexity: O(N)
# Space Complexity: O(N)