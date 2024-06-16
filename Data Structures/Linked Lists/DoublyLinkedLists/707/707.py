# Define a class for a list node
class ListNode:
    # Define a method to initialize a list node
    def __init__(self, x):
        self.val = x
        self.next, self.prev = None, None

# Define a class for a doubly linked list
class MyLinkedList:
    # Define a method to initialize a doubly linked list
    def __init__(self):
        self.size = 0
        # Sentinel nodes as pseudo-head and pseudo-tail
        self.head, self.tail = ListNode(0), ListNode(0) 
        self.head.next = self.tail
        self.tail.prev = self.head

    # Define a method to add an element at a specific index
    def addAtIndex(self, index: int, val: int) -> None:
        # If the index is greater than the length of the list, do not insert anything
        if index > self.size:
            return
        
        # If the index is negative, insert the element at the head of the list
        if index < 0:
            index = 0
        
        # Find the predecessor and successor of the node to be added
        if index < self.size - index:
            pred, succ = self.head, self.head.next
            for _ in range(index):
                pred, succ = succ, succ.next
        else:
            pred, succ = self.tail, self.tail.prev
            for _ in range(self.size - index):
                pred, succ = succ, succ.prev
        
        # Insert the node
        self.size += 1
        to_add = ListNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add

    # Define a method to delete an element at a specific index
    def deleteAtIndex(self, index: int) -> None:
        # If the index is out of range, do not delete anything
        if index < 0 or index >= self.size:
            return
        
        # Find the predecessor and successor of the node to be deleted
        if index < self.size - index:
            pred, succ = self.head, self.head.next
            for _ in range(index):
                pred, succ = succ, succ.next
        else:
            pred, succ = self.tail, self.tail.prev
            for _ in range(self.size - index):
                pred, succ = succ, succ.prev
        
        # Delete the node
        self.size -= 1
        pred.next = succ.next
        succ.next.prev = pred

# Time complexity: O(min(index, size - index)) for addAtIndex and deleteAtIndex
# Space complexity: O(1) for addAtIndex and deleteAtIndex