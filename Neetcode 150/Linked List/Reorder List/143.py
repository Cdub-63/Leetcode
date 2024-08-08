class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Reorders a singly linked list in-place such that the nodes are arranged in the following order:
        L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...
        
        Args:
            head (Optional[ListNode]): The head of the linked list to be reordered.
        
        Returns:
            None
        """
        
        # If the list is empty or has only one node, there is nothing to reorder.
        if not head or not head.next:
            return
        
        # Find the middle node of the list.
        # This is done by using two pointers, slow and fast, that move at different speeds.
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # Split the list into two halves.
        # The second half will be reversed later.
        second = slow.next
        slow.next = None
        
        # Reverse the second half of the list.
        # This is done by iteratively modifying the next pointers of the nodes.
        prev = None
        while second:
            # Store a reference to the next node.
            temp = second.next
            # Reverse the link by pointing the current node to the previous node.
            second.next = prev
            # Move the previous and current pointers one step forward.
            prev = second
            second = temp
        
        # Merge the two halves alternately.
        # This is done by iteratively modifying the next pointers of the nodes.
        first = head
        second = prev
        while second:
            # Store references to the next nodes in each half.
            temp1, temp2 = first.next, second.next
            # Reverse the link by pointing the current node in the first half to the current node in the second half.
            first.next = second
            second.next = temp1
            # Move the pointers to the next nodes in each half.
            first, second = temp1, temp2

# time complexity: O(n)
# space complexity: O(1)