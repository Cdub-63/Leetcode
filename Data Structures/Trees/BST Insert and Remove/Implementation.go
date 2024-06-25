package main

// TreeNode represents a node in a binary search tree.
type TreeNode struct {
    Val   int       // Value of the node
    Left  *TreeNode // Pointer to the left child
    Right *TreeNode // Pointer to the right child
}

// NewTreeNode creates and returns a new TreeNode with the given value.
func NewTreeNode(val int) *TreeNode {
    return &TreeNode{
        Val: val,
    }
}

// InsertAndRemove struct doesn't hold any data but provides methods for BST operations.
type InsertAndRemove struct {
}

// Insert a new node with the given value into the BST and return the root of the modified tree.
func (ir *InsertAndRemove) Insert(root *TreeNode, val int) *TreeNode {
    // If the current node is nil, create a new node with the value.
    if root == nil {
        return NewTreeNode(val)
    }

    // If the value is greater than the current node's value, insert it into the right subtree.
    if val > root.Val {
        root.Right = ir.Insert(root.Right, val)
    } else if val < root.Val { // If the value is less, insert it into the left subtree.
        root.Left = ir.Insert(root.Left, val)
    }
    // Return the root of the tree after insertion.
    return root
}

// MinValueNode returns the node with the minimum value found in the BST.
func (ir *InsertAndRemove) MinValueNode(root *TreeNode) *TreeNode {
    curr := root
    // Traverse to the leftmost node, which has the minimum value.
    while curr != nil && curr.Left != nil {
        curr = curr.Left
    }
    return curr
}

// Remove a node with the given value from the BST and return the root of the modified tree.
func (ir *InsertAndRemove) Remove(root *TreeNode, val int) *TreeNode {
    // If the root is nil, the tree is empty, return nil.
    if root == nil {
        return nil
    }

    // If the value to be removed is greater than the root's value, search in the right subtree.
    if val > root.Val {
        root.Right = ir.Remove(root.Right, val)
    } else if val < root.Val { // If less, search in the left subtree.
        root.Left = ir.Remove(root.Left, val)
    } else {
        // Node with only one child or no child
        if root.Left == nil {
            return root.Right
        } else if root.Right == nil {
            return root.Left
        }

        // Node with two children: Get the inorder successor (smallest in the right subtree)
        minNode := ir.MinValueNode(root.Right)

        // Copy the inorder successor's content to this node
        root.Val = minNode.Val

        // Delete the inorder successor
        root.Right = ir.Remove(root.Right, minNode.Val)
    }
    // Return the root of the tree after deletion.
    return root
}

// time complexity: O(h), where h is the height of the tree.
// space complexity: O(h), where h is the height of the tree.