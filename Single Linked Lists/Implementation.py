# Define a class for a list node
class ListNode:
    # Define a method to initialize a list node
    def __init__(self, val):
        self.val = val
        self.next = None

# Define a class for a singly linked list
class LinkedList:
    # Define a method to initialize a singly linked list
    def __init__(self):
        # Init the list with a 'dummy' node which makes 
        # removing a node from the beginning of list easier.
        self.head = ListNode(-1)
        self.tail = self.head
    
    # Define a method to insert a node at the end of the list
    def insertEnd(self, val):
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    # Define a method to remove a node at a specific index
    def remove(self, index):
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next
        
        # Remove the node ahead of curr
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next

    # Define a method to print the list
    def print(self):
        curr = self.head.next
        while curr:
            print(curr.val, " -> ", end="")
            curr = curr.next
        print()