class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Given the root of a binary search tree (BST) and an integer k, return the kth smallest value 
        (1-indexed) of all the values of the nodes in the tree.

        Args:
            root (Optional[TreeNode]): The root node of the binary search tree.
            k (int): The index of the kth smallest element.

        Returns:
            int: The kth smallest element in the binary search tree.
        """
        # Initialize an empty stack to keep track of the nodes to be visited.
        stack = []
        # Initialize a variable to keep track of the current node.
        curr = root

        # Keep traversing the binary search tree until we have found the kth smallest element.
        while stack or curr:
            # Traverse as far left as possible from the current node.
            # This ensures that we are always considering the leftmost nodes first.
            while curr:
                # Add the current node to the stack to be visited later.
                stack.append(curr)
                # Move to the left child of the current node.
                curr = curr.left
            # Pop the leftmost node from the stack and move to its right child.
            # This ensures that we are always considering the right child next.
            curr = stack.pop()
            # Decrement the count of nodes to be visited.
            k -= 1
            # If we have found the kth smallest element, return its value.
            if k == 0:
                return curr.val
            # Move to the right child of the current node.
            curr = curr.right

# Time Complexity: O(N)
# Space Complexity: O(N)