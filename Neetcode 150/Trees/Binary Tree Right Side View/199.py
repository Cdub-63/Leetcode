class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        """
        This function takes in the root of a binary tree and returns a list of the rightmost
        elements at each level of the tree. The rightmost elements are the last elements that
        are visible when looking at the tree from the right side.
        """
        res = []
        q = collections.deque([root])

        while q:
            rightSide = None
            qLen = len(q)

            # Iterate over the nodes at the current level
            for i in range(qLen):
                node = q.popleft()
                if node:
                    # Keep track of the rightmost element at the current level
                    rightSide = node
                    # Append the left and right children of the current node to the queue
                    q.append(node.left)
                    q.append(node.right)
            # If there are nodes at the current level, add the rightmost element to the result
            if rightSide:
                res.append(rightSide.val)
        return res

# time complexity: O(N)
# space complexity: O(N)