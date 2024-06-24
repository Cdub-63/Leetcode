package main

import "fmt"

// TreeNode represents a node in the binary search tree.
type TreeNode struct {
    Val   int
    Left  *TreeNode
    Right *TreeNode
}

// deleteNode deletes a node with the given key from the BST and returns the root of the modified tree.
func deleteNode(root *TreeNode, key int) *TreeNode {
    if root == nil {
        // Base case: if the tree is empty or the node is not found.
        return nil
    }
    if key < root.Val {
        // If the key to delete is less than the root's value, go left.
        root.Left = deleteNode(root.Left, key)
    } else if key > root.Val {
        // If the key to delete is greater than the root's value, go right.
        root.Right = deleteNode(root.Right, key)
    } else {
        // Found the node to delete.
        if root.Left == nil {
            // If the node has no left child, return the right child.
            return root.Right
        } else if root.Right == nil {
            // If the node has no right child, return the left child.
            return root.Left
        }
        // If the node has two children, find the in-order successor (smallest in the right subtree).
        minNode := findMin(root.Right)
        // Replace the value of the node to delete with the in-order successor's value.
        root.Val = minNode.Val
        // Delete the in-order successor.
        root.Right = deleteNode(root.Right, root.Val)
    }
    return root
}

// findMin finds the node with the minimum value in a BST (leftmost node).
func findMin(node *TreeNode) *TreeNode {
    for node.Left != nil {
        node = node.Left
    }
    return node
}

// Time complexity: O(h), where h is the height of the tree.
// Space complexity: O(h)