class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # If the root node is None, the tree is empty, so return None.
        if not root:
            return None
        
        # Swap the left and right children of the root node.
        # This is the core operation of the tree inversion.
        # Before, the left subtree was the left child and the right subtree was the right child.
        # After, the left subtree is the right child and the right subtree is the left child.
        root.left, root.right = root.right, root.left
        
        # Recursively invert the left and right subtrees.
        # This is necessary because the tree inversion operation needs to be applied to all nodes in the tree.
        # We can't just swap the children of the root node and be done with it.
        # We need to recursively traverse the tree and swap the children of all nodes.
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        # Return the root node after the tree inversion operation has been completed.
        # The root node now has its left and right children swapped.
        # The left subtree is now the right subtree and the right subtree is now the left subtree.
        return root

# Time complexity: O(n)
# Space complexity: O(n)