# Define a class for the nodes in the binary search tree
class TreeNode:
    # Initialize a tree node with a value and two children
    def __init__(self, val):
        self.val = val  # The value stored in the node
        self.left = None  # Initialize the left child as None
        self.right = None  # Initialize the right child as None

# Function to perform a binary search in the tree
def search(root, target):
    if not root:  # If the tree or subtree is empty, the target is not found
        return False

    # Compare the target with the root's value
    if target > root.val:  # If the target is greater, search the right subtree
        return search(root.right, target)
    elif target < root.val:  # If the target is smaller, search the left subtree
        return search(root.left, target)
    else:  # If the target is equal to the root's value, the target is found
        return True
    
# time complexity: O(h), where h is the height of the tree
# space complexity: O(h), where h is the height of the tree