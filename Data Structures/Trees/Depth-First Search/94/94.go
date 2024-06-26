package main

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// inorderTraversal performs an in-order traversal of a binary tree and returns the values of the nodes in the tree in an
func inorderTraversal(root *TreeNode) []int {
	// If the root is nil, return an empty slice
	if root == nil {
		return []int{}
	}
	// Create an empty slice to store the inorder traversal
	inorder := []int{}
	// Perform an in-order traversal and append the values to the slice
	inorder = append(inorder, inorderTraversal(root.Left)...)
	inorder = append(inorder, root.Val)
	inorder = append(inorder, inorderTraversal(root.Right)...)
	// Return the inorder traversal
	return inorder
}

// time complexity: O(n)
// space complexity: O(n)
