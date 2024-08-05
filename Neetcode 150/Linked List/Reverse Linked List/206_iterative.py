class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverses a singly linked list.
        
        Args:
            head (Optional[ListNode]): The head of the linked list to be reversed.
        
        Returns:
            Optional[ListNode]: The head of the reversed linked list.
        """
        
        # Initialize a variable to keep track of the previous node
        prev = None
        
        # Initialize a variable to keep track of the current node
        current = head
        
        # Iterate over the linked list
        while current:
            # Store a reference to the next node
            next_temp = current.next
            
            # Reverse the link by pointing the current node to the previous node
            current.next = prev
            
            # Move the previous and current pointers one step forward
            prev = current
            current = next_temp
        
        # Return the new head of the reversed linked list
        return prev

# Time complexity: O(n)
# Space complexity: O(1)