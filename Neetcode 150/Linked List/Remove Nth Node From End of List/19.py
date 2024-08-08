# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Given a singly linked list and an integer 'n', this function removes the nth node from the end 
        of the list and returns the modified list.
        
        Parameters:
            head (Optional[ListNode]): The head of the linked list.
            n (int): The index of the node to be removed.
        
        Returns:
            Optional[ListNode]: The modified linked list with the nth node removed.
        """
        # Create two pointers, 'fast' and 'slow', to traverse the list.
        fast = slow = head
        
        # Move the 'fast' pointer 'n' steps ahead in the list.
        for _ in range(n):
            fast = fast.next  # Move 'fast' pointer to the next node.
        
        # If the 'fast' pointer has reached the end of the list, it means we need to remove the head node.
        if not fast:
            return head.next  # Remove the head node by pointing the head to the next node.
        
        # Move both 'fast' and 'slow' pointers until 'fast' reaches the end of the list.
        while fast.next:
            fast = fast.next  # Move 'fast' pointer to the next node.
            slow = slow.next  # Move 'slow' pointer to the next node.
        
        # Remove the nth node from the end of the list.
        slow.next = slow.next.next  # Point the 'next' pointer of the 'slow' node to the node after the nth node.
        
        return head  # Return the modified linked list.

# Time Complexity: O(N)
# Space Complexity: O(1)