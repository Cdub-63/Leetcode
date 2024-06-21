package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func searchBST(root *TreeNode, val int) *TreeNode {
	// If the tree is empty, return nil
	if root == nil {
		return nil
	}

	// If the root's value is equal to the target value, return the root
	if root.Val == val {
		return root
	}

	// If the root's value is greater than the target value, search the left subtree
	if root.Val > val {
		return searchBST(root.Left, val)
	}

	// If the root's value is less than the target value, search the right subtree
	return searchBST(root.Right, val)
}

// Time complexity: O(h), where h is the height of the tree
// Space complexity: O(h), where h is the height of the tree
