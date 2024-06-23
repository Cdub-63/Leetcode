package main

import "fmt"

// TreeNode represents a node in the binary search tree.
type TreeNode struct {
    Val   int
    Left  *TreeNode
    Right *TreeNode
}

// insertIntoBST inserts a new value into the BST and returns the root of the modified tree.
func insertIntoBST(root *TreeNode, val int) *TreeNode {
    // If the root is nil, the new value becomes the root.
    if root == nil {
        return &TreeNode{Val: val}
    }
    // If the value is less than the current node's value, insert it into the left subtree.
    if val < root.Val {
        root.Left = insertIntoBST(root.Left, val)
    } else {
        // Otherwise, insert it into the right subtree.
        root.Right = insertIntoBST(root.Right, val)
    }
    // Return the unchanged root node.
    return root
}

// Time complexity: O(h), where h is the height of the tree.
// Space complexity: O(h)