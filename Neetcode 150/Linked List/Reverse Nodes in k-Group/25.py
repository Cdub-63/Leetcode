class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Check if we have enough nodes to reverse
        # Start at head and move k nodes forward
        # If we reach the end of the list before k nodes, return the original list
        curr = head
        for _ in range(k):
            if not curr:  # If we reach the end of the list before k nodes, return the original list
                return head
            curr = curr.next
        
        # We have enough nodes to reverse, so reverse the next k nodes
        # Store the previous node and the current node
        # Move the current node k-1 steps forward
        # Store the next node and update the current node's next pointer
        # Repeat until we have reversed all k nodes
        prev = None
        curr = head
        for _ in range(k):
            # Store the next node
            next_node = curr.next
            # Reverse the link by pointing the current node to the previous node
            curr.next = prev
            # Move the previous and current pointers one step forward
            prev = curr
            curr = next_node
        
        # Recursively reverse the next group of nodes
        # The current head now points to the reversed group
        # So we connect the reversed group to the remaining nodes after the reversed group
        # The new head of the reversed group is the previous node
        head.next = self.reverseKGroup(curr, k)
        
        # Return the new head of the reversed group
        return prev

# time complexity: O(n)
# space complexity: O(1)