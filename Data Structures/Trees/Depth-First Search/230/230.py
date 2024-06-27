# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """
        Initialize a new TreeNode with the given value and left and right child nodes.
        
        Args:
            val (int): The value to be assigned to the TreeNode.
            left (TreeNode): The left child of the TreeNode (default: None).
            right (TreeNode): The right child of the TreeNode (default: None).
        """
        # Assign the given value to the TreeNode's val attribute
        self.val = val
        
        # Assign the given left child to the TreeNode's left attribute
        self.left = left
        
        # Assign the given right child to the TreeNode's right attribute
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Initialize an empty stack to keep track of the nodes to be visited
        stack = []
        
        # Initialize a variable to keep track of the current node
        curr = root
        
        # Keep traversing the binary search tree until we have found the kth smallest element
        while stack or curr:
            
            # Traverse as far left as possible from the current node
            # This ensures that we are always considering the leftmost nodes first
            while curr:
                # Add the current node to the stack to be visited later
                stack.append(curr)
                
                # Move to the left child of the current node
                curr = curr.left
            
            # Pop the leftmost node from the stack and move to its right child
            # This ensures that we are always considering the right child next
            curr = stack.pop()
            
            # Decrement the count of nodes to be visited
            k -= 1
            
            # If we have found the kth smallest element, return its value
            if k == 0:
                return curr.val
            
            # Move to the right child of the current node
            curr = curr.right

# Time Complexity: O(N)
# Space Complexity: O(N)