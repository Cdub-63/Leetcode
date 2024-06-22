class TreeNode:
    # Constructor to initialize a node
    def __init__(self, val):
        self.val = val  # Value of the node
        self.left = None  # Pointer to the left child
        self.right = None  # Pointer to the right child

# Function to insert a new node with a given value into the BST.
def insert(root, val):
    # If the current node is None, create a new node with the value and return it.
    if not root:
        return TreeNode(val)
    
    # If the value to insert is greater than the current node's value, insert it into the right subtree.
    if val > root.val:
        root.right = insert(root.right, val)
    # If the value to insert is less than the current node's value, insert it into the left subtree.
    elif val < root.val:
        root.left = insert(root.left, val)
    # Return the (possibly updated) current node.
    return root

# Function to find the node with the minimum value in the BST.
def minValueNode(root):
    curr = root  # Start with the current node as the root.
    # Loop to find the leftmost leaf, which is the minimum value node in the BST.
    while curr and curr.left:
        curr = curr.left
    # Return the node with the minimum value.
    return curr

# Function to remove a node with a given value from the BST.
def remove(root, val):
    # If the root is None, the tree is empty, so return None.
    if not root:
        return None
    
    # If the value to remove is greater than the current node's value, go to the right subtree.
    if val > root.val:
        root.right = remove(root.right, val)
    # If the value to remove is less than the current node's value, go to the left subtree.
    elif val < root.val:
        root.left = remove(root.left, val)
    else:
        # If the node to be deleted is a leaf or has one child, replace it with its child.
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        # If the node has two children, replace it with its in-order successor.
        else:
            minNode = minValueNode(root.right)  # Find the in-order successor.
            root.val = minNode.val  # Copy the in-order successor's value to this node.
            root.right = remove(root.right, minNode.val)  # Delete the in-order successor.
    # Return the (possibly updated) root.
    return root

# time complexity: O(h), where h is the height of the BST.
# space complexity: O(h), where h is the height of the BST.