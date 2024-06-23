# Definition for a binary tree node.
class TreeNode:
    # Initialize a tree node with value, left child, and right child.
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # Node's value
        self.left = left  # Left child
        self.right = right  # Right child

class Solution:
    # Function to insert a value into a binary search tree (BST) and return the root of the modified tree.
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # If the current node is None, create a new node with the value and return it.
        # This is the base case for recursion.
        if not root:
            return TreeNode(val)
        
        # If the value to insert is greater than the current node's value,
        # insert the value in the right subtree.
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            # If the value is less than or equal to the current node's value,
            # insert the value in the left subtree.
            root.left = self.insertIntoBST(root.left, val)
        
        # Return the unchanged current node.
        return root
    
# Time complexity: O(H), where H is the height of the tree.
# This is because in the worst case, we have to travel from the root to the leaf.
# Space complexity: O(H) due to the recursion stack.
# In the worst case (a skewed tree), the recursion stack could be as large as the height of the tree.