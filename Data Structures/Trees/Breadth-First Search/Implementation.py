from collections import deque

class TreeNode:
    def __init__(self, val):
        """
        Initialize a new TreeNode with the given value and initialize its left and right child nodes as None.
        
        Args:
            val (int): The value to be assigned to the TreeNode.
        """
        
        # Assign the given value to the TreeNode's val attribute
        self.val = val
        
        # Initialize the left child of the TreeNode as None
        self.left = None
        
        # Initialize the right child of the TreeNode as None
        self.right = None

def bfs(root):
    # Create a queue to store the nodes of the tree
    queue = deque()

    # Check if the root exists
    if root:
        # Add the root node to the queue
        queue.append(root)
    
    # Initialize the level variable to 0
    level = 0
    
    # Loop until the queue is empty
    while len(queue) > 0:
        # Print the current level
        print("Level: ", level)

        # Loop through each node in the queue
        for i in range(len(queue)):
            # Remove the node from the front of the queue
            node = queue.popleft()
            
            # Print the value of the current node
            print(node.val)

            # Check if the left child of the current node exists
            if node.left:
                # Add the left child to the back of the queue
                queue.append(node.left)
            
            # Check if the right child of the current node exists
            if node.right:
                # Add the right child to the back of the queue
                queue.append(node.right)
        
        # Increment the level after processing all nodes in the current level
        level += 1
