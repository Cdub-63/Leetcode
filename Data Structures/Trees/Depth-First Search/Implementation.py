class TreeNode:
    def __init__(self, val):
        """
        Initialize a new TreeNode with the given value.

        Args:
            val (int): The value to be assigned to the node.

        Returns:
            None
        """
        self.val = val
        self.left = None
        self.right = None

def inorder(root):
    """
    Perform an inorder traversal of a binary tree.

    Args:
        root (TreeNode): The root node of the binary tree.

    Returns:
        None
    """
    if not root:
        return
    inorder(root.left)  # Traverse left subtree
    print(root.val)     # Print value of current node
    inorder(root.right) # Traverse right subtree

def preorder(root):
    """
    Perform a preorder traversal of a binary tree.

    Args:
        root (TreeNode): The root node of the binary tree.

    Returns:
        None
    """
    if not root:
        return
    print(root.val)     # Print value of current node
    preorder(root.left) # Traverse left subtree
    preorder(root.right) # Traverse right subtree

def postorder(root):
    """
    Perform a postorder traversal of a binary tree.

    Args:
        root (TreeNode): The root node of the binary tree.

    Returns:
        None
    """
    if not root:
        return
    postorder(root.left)  # Traverse left subtree
    postorder(root.right) # Traverse right subtree
    print(root.val)       # Print value of current node

# time complexity: O(n)
# space complexity: O(n)