# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # If the tree is empty, return None
        if root is None:
            return None

        # If the root's value is equal to the target value, return the root
        if root.val == val:
            return root

        # If the root's value is greater than the target value, search the left subtree
        if root.val > val:
            return self.searchBST(root.left, val)

        # If the root's value is less than the target value, search the right subtree
        return self.searchBST(root.right, val)
    
# time complexity: O(h), where h is the height of the tree
# space complexity: O(h), where h is the height of the tree