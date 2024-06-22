package main

import (
	"fmt"
)

// DoublyLinkedListNode is the node type for a doubly linked list
type DoublyLinkedListNode struct {
	val  int
	next *DoublyLinkedListNode
	prev *DoublyLinkedListNode
}

// DoublyLinkedList is the structure for a doubly linked list
type DoublyLinkedList struct {
	head *DoublyLinkedListNode
	tail *DoublyLinkedListNode
}

// NewDoublyLinkedListNode creates a new doubly linked list node
func NewDoublyLinkedListNode(val int) *DoublyLinkedListNode {
	return &DoublyLinkedListNode{
		val:  val,
		next: nil,
		prev: nil,
	}
}

// NewDoublyLinkedList creates a new doubly linked list
func NewDoublyLinkedList() *DoublyLinkedList {
	head := NewDoublyLinkedListNode(-1)
	tail := NewDoublyLinkedListNode(-1)
	head.next = tail
	tail.prev = head
	return &DoublyLinkedList{
		head: head,
		tail: tail,
	}
}

// InsertFront inserts a new node at the front of the list
func (d *DoublyLinkedList) InsertFront(val int) {
	newNode := NewDoublyLinkedListNode(val)
	newNode.prev = d.head
	newNode.next = d.head.next

	d.head.next.prev = newNode
	d.head.next = newNode
}

// InsertEnd inserts a new node at the end of the list
func (d *DoublyLinkedList) InsertEnd(val int) {
	newNode := NewDoublyLinkedListNode(val)
	newNode.next = d.tail
	newNode.prev = d.tail.prev

	d.tail.prev.next = newNode
	d.tail.prev = newNode
}

// RemoveFront removes the node at the front of the list
func (d *DoublyLinkedList) RemoveFront() {
	if d.head.next != d.tail {
		d.head.next.next.prev = d.head
		d.head.next = d.head.next.next
	}
}

// RemoveEnd removes the node at the end of the list
func (d *DoublyLinkedList) RemoveEnd() {
	if d.tail.prev != d.head {
		d.tail.prev.prev.next = d.tail
		d.tail.prev = d.tail.prev.prev
	}
}

// Print prints the doubly linked list
func (d *DoublyLinkedList) Print() {
	curr := d.head.next
	for curr != d.tail {
		fmt.Printf("%d -> ", curr.val)
		curr = curr.next
	}
	fmt.Println()
}
