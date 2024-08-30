class Codec:
    def serialize(self, root):
        res = []
        def dfs(node):
            if not node:
                res.append("N")  # Append "N" for null nodes
                return
            res.append(str(node.val))  # Append the node's value
            dfs(node.left)  # Recursively serialize left subtree
            dfs(node.right)  # Recursively serialize right subtree
        dfs(root)
        return ",".join(res)  # Join all values with commas

    def deserialize(self, data):
        vals = data.split(",")  # Split the string into a list of values
        self.i = 0  # Initialize index for traversing the values
        
        def dfs():
            if vals[self.i] == "N":  # If the value is "N", it's a null node
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))  # Create a new node with the current value
            self.i += 1
            node.left = dfs()  # Recursively construct left subtree
            node.right = dfs()  # Recursively construct right subtree
            return node
        
        return dfs()  # Start the deserialization process

# Time complexity: O(N) where N is the number of nodes in the tree
# Space complexity: O(N) where N is the number of nodes in the tree