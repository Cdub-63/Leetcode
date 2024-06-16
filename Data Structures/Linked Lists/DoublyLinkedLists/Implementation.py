# Define a class for a list node
class ListNode:
    # Define a method to initialize a list node
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

# Define a class for a doubly linked list
class LinkedList:
    # Define a method to initialize a doubly linked list
    def __init__(self):
        # Initialize the list with 'dummy' head and tail nodes which makes 
        # edge cases for insert & remove easier.
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    # Define a method to insert a node at the front of the list
    def insertFront(self, val):
        newNode = ListNode(val)
        newNode.prev = self.head
        newNode.next = self.head.next

        self.head.next.prev = newNode
        self.head.next = newNode

    # Define a method to insert a node at the end of the list
    def insertEnd(self, val):
        newNode = ListNode(val)
        newNode.next = self.tail
        newNode.prev = self.tail.prev

        self.tail.prev.next = newNode
        self.tail.prev = newNode

    # Define a method to remove the first node after the dummy head (assume it exists)
    def removeFront(self):
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next

    # Define a method to remove the last node before the dummy tail (assume it exists)
    def removeEnd(self):
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev

    # Define a method to print the list
    def print(self):
        curr = self.head.next
        while curr != self.tail:
            print(curr.val, " -> ")
            curr = curr.next
        print()

#time complexity: O(1) for all operations
#space complexity: O(1) for all operations