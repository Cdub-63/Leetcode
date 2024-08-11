class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Check if the linked list is empty or has only one node.
        # If so, there cannot be a cycle.
        if not head or not head.next:
            return False
        
        # Initialize two pointers: 'tortoise' and 'hare'.
        # The 'tortoise' pointer moves one step at a time, while the 'hare' pointer moves two steps at a time.
        # They are used to check for a cycle in the linked list.
        tortoise = head
        hare = head.next
        
        # Continue iterating until the two pointers meet or one of them reaches the end of the list.
        while tortoise != hare:
            # If the 'hare' pointer reaches the end of the list, there cannot be a cycle.
            if not hare or not hare.next:
                return False
            
            # Move the 'tortoise' pointer to the next node.
            tortoise = tortoise.next
            
            # Move the 'hare' pointer to the node after the next node.
            hare = hare.next.next
        
        # If the two pointers meet, a cycle has been found.
        return True

# time complexity: O(n)
# space complexity: O(1)