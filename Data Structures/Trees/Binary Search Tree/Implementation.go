// Declare the main package
package main

// Define a struct for the nodes in the binary search tree
type TreeNode struct {
	Val   int       // The value stored in the node
	Left  *TreeNode // Pointer to the left child node
	Right *TreeNode // Pointer to the right child node
}

// Function to create a new tree node
func NewTreeNode(val int) *TreeNode {
	return &TreeNode{
		Val:   val, // Set the node's value
		Left:  nil, // Initialize the left child as nil
		Right: nil, // Initialize the right child as nil
	}
}

// Define a struct for the search operation
type Search struct{}

// Method to perform a binary search in the tree
func (s *Search) Search(root *TreeNode, target int) bool {
	if root == nil { // If the tree or subtree is empty, the target is not found
		return false
	}

	// Compare the target with the root's value
	if target > root.Val { // If the target is greater, search the right subtree
		return s.Search(root.Right, target)
	} else if target < root.Val { // If the target is smaller, search the left subtree
		return s.Search(root.Left, target)
	} else { // If the target is equal to the root's value, the target is found
		return true
	}
}

// Time complexity: O(h), where h is the height of the tree
// Space complexity: O(h), where h is the height of the tree
