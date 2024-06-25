# Definition for a binary tree node.
class TreeNode:
    # Initialize a tree node with value, left child, and right child.
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # Node's value
        self.left = left  # Left child
        self.right = right  # Right child

class Solution:
    # Function to delete a node from a binary search tree (BST) and return the root of the modified tree.
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # If the root is None, the tree is empty or we've reached a leaf node, return None.
        if not root:
            return root
        
        # If the key to delete is greater than the root's value, delete from the right subtree.
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        # If the key to delete is less than the root's value, delete from the left subtree.
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # If the current node is the one to delete
            # Case 1: Node has no left child, return the right child to reconnect the tree.
            if not root.left:
                return root.right
            # Case 2: Node has no right child, return the left child to reconnect the tree.
            elif not root.right:
                return root.left
            
            # Case 3: Node has two children, find the in-order successor (smallest in the right subtree)
            cur = root.right
            while cur.left:
                cur = cur.left
            # Replace the value of the node to be deleted with the in-order successor's value.
            root.val = cur.val
            # Delete the in-order successor
            root.right = self.deleteNode(root.right, root.val)
        # Return the root of the modified tree.
        return root
    
# Time complexity: O(H), where H is the height of the tree.
# Space complexity: O(H), where H is the height of the tree.