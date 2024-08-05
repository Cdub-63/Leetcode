class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Recursively reverses a singly linked list.
        
        Args:
            head (Optional[ListNode]): The head of the linked list to be reversed.
        
        Returns:
            Optional[ListNode]: The head of the reversed linked list.
        """
        
        # Base case: If the linked list is empty or has only one node,
        # return the head itself since reversing it doesn't change anything.
        if not head or not head.next:
            return head
        
        # Recursive case: If the linked list has more than one node,
        # recursively reverse the tail of the list.
        new_head = self.reverseList(head.next)
        
        # After recursively reversing the tail, the new head of the reversed list
        # is the current head's next node.
        # By pointing the next node of the current head to the current head itself,
        # we effectively reverse the link between the current head and its next node.
        head.next.next = head
        
        # By setting the next node of the current head to None,
        # we break the link between the current head and its next node in the original list.
        head.next = None
        
        # Finally, return the new head of the reversed list, which is the head of the original list
        # after the recursive call.
        return new_head

# Time complexity: O(n)
# Space complexity: O(n)