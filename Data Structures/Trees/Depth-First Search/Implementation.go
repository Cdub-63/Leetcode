package main

import "fmt"

// TreeNode represents a node in a binary tree
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// NewTreeNode creates a new TreeNode with the given value
func NewTreeNode(val int) *TreeNode {
	return &TreeNode{
		Val:   val,
		Left:  nil,
		Right: nil,
	}
}

// DFS represents a depth-first search object
type DFS struct {}

// InOrder performs an in-order traversal of a binary tree
func (dfs *DFS) InOrder(root *TreeNode) {
	if root == nil {
		return
	}
	dfs.InOrder(root.Left) // Traverse left subtree
	fmt.Print(root.Val)   // Print the current node's value
	dfs.InOrder(root.Right) // Traverse right subtree
}

// PreOrder performs a pre-order traversal of a binary tree
func (dfs *DFS) PreOrder(root *TreeNode) {
	if root == nil {
		return
	}
	fmt.Print(root.Val)   // Print the current node's value
	dfs.PreOrder(root.Left) // Traverse left subtree
	dfs.PreOrder(root.Right) // Traverse right subtree
}

// PostOrder performs a post-order traversal of a binary tree
func (dfs *DFS) PostOrder(root *TreeNode) {
	if root == nil {
		return
	}
	dfs.PostOrder(root.Left) // Traverse left subtree
	dfs.PostOrder(root.Right) // Traverse right subtree
	fmt.Print(root.Val)   // Print the current node's value
}

// time complexity: O(n)
// space complexity: O(n)