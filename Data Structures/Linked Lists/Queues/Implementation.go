package main

import (
	"fmt"
	"os"
)

type ListNode struct {
	Val  int
	Next *ListNode
}

type Queue struct {
	Left  *ListNode // front of Queue
	Right *ListNode // back of Queue
}

func NewQueue() *Queue {
	return &Queue{
		Left:  nil,
		Right: nil,
	}
}

func NewListNode(val int) *ListNode {
	return &ListNode{
		Val:  val,
		Next: nil,
	}
}

func (q *Queue) Enqueue(val int) {
	newNode := NewListNode(val)
	if q.Right != nil {
		// Queue is not empty
		q.Right.Next = newNode
		q.Right = q.Right.Next
	} else {
		// Queue is empty
		q.Left = newNode
		q.Right = newNode
	}
}

func (q *Queue) Dequeue() int {
	if q.Left == nil {
		// Queue is empty
		os.Exit(0)
	}
	val := q.Left.Val
	q.Left = q.Left.Next
	if q.Left == nil {
		q.Right = nil
	}
	return val
}

func (q *Queue) Print() {
	cur := q.Left
	for cur != nil {
		fmt.Printf("%d -> ", cur.Val)
		cur = cur.Next
	}
	fmt.Println()
}
