class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to serve as the head of our resulting linked list
        dummy = ListNode(0)  # Initialize with a dummy node
        current = dummy  # Initialize a pointer to the dummy node
        carry = 0  # Initialize the carry variable
        
        # Loop until we have exhausted both input linked lists and there is no remaining carry
        while l1 or l2 or carry:
            # If there is a node in the first linked list, get its value, otherwise default to 0
            val1 = l1.val if l1 else 0
            # If there is a node in the second linked list, get its value, otherwise default to 0
            val2 = l2.val if l2 else 0
            
            # Calculate the total value of the two input values and the current carry
            total = val1 + val2 + carry
            # Calculate the new carry by taking the integer division of the total by 10
            carry = total // 10
            # Calculate the digit value by taking the remainder of the total when divided by 10
            digit = total % 10
            
            # Create a new node with the calculated digit value and add it to the linked list
            current.next = ListNode(digit)
            # Move the pointer to the next node in the linked list
            current = current.next
            
            # If there is a node in the first linked list, move the pointer to the next node
            if l1:
                l1 = l1.next
            # If there is a node in the second linked list, move the pointer to the next node
            if l2:
                l2 = l2.next
        
        # Return the head of the resulting linked list, skipping the dummy node
        return dummy.next

# Time Complexity: O(max(m, n))
# Space Complexity: O(max(m, n))