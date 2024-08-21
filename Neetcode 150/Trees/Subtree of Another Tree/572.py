class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Checks if the given subtree is present in the given tree.

        Parameters:
            root (Optional[TreeNode]): The root of the tree
            subRoot (Optional[TreeNode]): The root of the subtree to check

        Returns:
            bool: True if the subtree is present, False otherwise
        """
        # Base case: if both root and subRoot are None, they are the same
        if not root and not subRoot:
            return True  # They are both None, so the subtree is present
        # If either root or subRoot is None, they are not the same
        if not root or not subRoot:
            return False  # One of them is None, so the subtree is not present
        # Check if the current nodes are the same
        if self.isSameTree(root, subRoot):
            return True  # The current nodes are the same, so the subtree is present
        # If not, recursively check the left and right subtrees of the root
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        # We need to check both the left and right subtrees, so we use the "or" operator.
        # If the subtree is present in either subtree, we return True. Otherwise, we return False

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Checks if the given trees p and q are structurally identical.

        Parameters:
            p (Optional[TreeNode]): The root of the first tree
            q (Optional[TreeNode]): The root of the second tree

        Returns:
            bool: True if the trees are structurally identical, False otherwise
        """
        # Base case: if both p and q are None, they are the same tree
        if p is None and q is None:
            return True  # Both trees are None, so they are the same

        # If either p or q is None, they are not the same tree
        if p is None or q is None:
            return False  # One tree is None, so they are not the same

        # Check if the current nodes have the same value
        if p.val != q.val:
            return False  # The nodes have different values, so they are not the same tree

        # Recursively check the left and right subtrees of the trees
        return (self.isSameTree(p.left, q.left)  # Check if the left subtrees are the same
                and self.isSameTree(p.right, q.right))  # Check if the right subtrees are the same

# Time complexity: O(m * n), where m and n are the lengths of p and q respectively
# space complexity: O(h), where h is the height of the tree