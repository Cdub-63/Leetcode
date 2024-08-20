class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # If both trees are empty, they are the same.
        if not p and not q:
            return True

        # If one tree is empty and the other is not, they are not the same.
        if p and not q or q and not p:
            return False

        # If the values of the nodes are the same and the left and right subtrees are the same, 
        # then the two trees are the same.
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        # If the values of the nodes are different or the left or right subtrees are different, 
        # then the two trees are not the same.
        else:
            return False

# Time Complexity: O(n), where n is the number of nodes in the tree
# Space Complexity: O(h), where h is the height of the tree