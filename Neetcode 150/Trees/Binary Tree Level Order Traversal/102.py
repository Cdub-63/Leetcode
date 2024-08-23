class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # Initialize an empty list to store the result
        res = []
        # Initialize an empty queue to store the nodes
        q = collections.deque()
        # If the root is not None then add it to the queue
        if root:
            q.append(root)

        # While the queue is not empty
        while q:
            # Initialize an empty list to store the values of the nodes
            # in the current level
            val = []

            # Iterate over the nodes in the current level
            for i in range(len(q)):
                # Dequeue a node from the queue
                node = q.popleft()
                # Append the value of the node to the list
                val.append(node.val)
                # If the node has a left child then add it to the queue
                if node.left:
                    q.append(node.left)
                # If the node has a right child then add it to the queue
                if node.right:
                    q.append(node.right)

            # Append the list of values to the result
            res.append(val)

        # Return the result
        return res

# time complexity: O(N)
# space complexity: O(N)