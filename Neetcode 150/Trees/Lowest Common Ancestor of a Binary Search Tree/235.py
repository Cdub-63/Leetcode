class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # Start at the root of the binary search tree.
        # The lowest common ancestor (LCA) of p and q is a node that is:
        # 1. Greater than both p and q.
        # 2. Smaller than both p and q.
        # We will move down the tree until we find a node that satisfies these conditions.
        while True:
            # If the root's value is less than both p and q, move to the right.
            # This is because the LCA we are looking for should be in the right subtree.
            if root.val < p.val and root.val < q.val:
                root = root.right
            # If the root's value is greater than both p and q, move to the left.
            # This is because the LCA we are looking for should be in the left subtree.
            elif root.val > p.val and root.val > q.val:
                root = root.left
            # If the root's value is neither less than both p and q nor greater than both p and q,
            # then we have found the LCA.
            else:
                # This condition is equivalent to saying that the root is between p and q
                # (i.e., it is greater than or equal to p and less than or equal to q).
                # If the root's value is equal to one of the nodes p or q, then we have found the LCA.
                return root

# Time Complexity: O(h), where h is the height of the tree
# Space Complexity: O(1)