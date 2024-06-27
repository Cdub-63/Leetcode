package main

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// kthSmallest finds the kth smallest element in a binary search tree.
// The function takes in a pointer to the root of the binary search tree
// and an integer k indicating the kth smallest element to find.
// It returns an integer representing the kth smallest element.
func kthSmallest(root *TreeNode, k int) int {
	// Create a stack to store the nodes of the binary search tree.
	// Initialize the stack with a capacity of k.
	stack := make([]*TreeNode, 0, k)

	// Traverse the binary search tree in an in-order manner.
	// When we encounter a node, push it onto the stack.
	// Keep traversing the left subtree until we reach a leaf node.
	for {
		// Traverse the left subtree until we reach a leaf node.
		for root != nil {
			// Push the current node onto the stack.
			stack = append(stack, root)
			// Move to the left subtree.
			root = root.Left
		}

		// If the stack is empty, it means we have reached the end of
		// the binary search tree.
		if len(stack) == 0 {
			break
		}

		// Pop the top node from the stack.
		root = stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		// Decrement the value of k.
		k--

		// If k becomes 0, it means we have found the kth smallest element.
		if k == 0 {
			return root.Val
		}

		// Traverse the right subtree.
		root = root.Right
	}

	// If we reach this point, it means the binary search tree is empty or
	// the value of k is greater than the number of nodes in the tree.
	return -1
}

// Time Complexity: O(n)
// Space Complexity: O(n)
