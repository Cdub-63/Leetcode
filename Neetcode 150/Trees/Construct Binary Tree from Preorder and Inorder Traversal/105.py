class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Check if the preorder or inorder lists are empty. If they are, return None.
        if not preorder or not inorder:
            return None

        # Create a new TreeNode using the first element of the preorder list as the root value.
        root = TreeNode(preorder[0])

        # Find the index of the root value in the inorder list. This will be used to split the inorder list into two parts.
        mid = inorder.index(preorder[0])

        # Recursively call buildTree on the left subtree of the root.
        # The left subtree is the part of the preorder and inorder lists that come before the root value.
        # The left subtree is constructed using the elements of the preorder list from index 1 to mid (inclusive).
        # The left subtree is constructed using the elements of the inorder list from index 0 to mid (exclusive).
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])

        # Recursively call buildTree on the right subtree of the root.
        # The right subtree is the part of the preorder and inorder lists that come after the root value.
        # The right subtree is constructed using the elements of the preorder list from index mid + 1 to the end.
        # The right subtree is constructed using the elements of the inorder list from index mid + 1 to the end.
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])

        # Return the root of the constructed binary tree.
        return root

# Time Complexity: O(n)
# Space Complexity: O(n)