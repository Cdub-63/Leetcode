# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # Define a method to reverse a linked list
    def reverseList(self, head: ListNode) -> ListNode:
        # Initialize previous and current pointers
        prev = None
        curr = head

        # Iterate over the linked list
        while curr:
            # Remember the next node
            next_node = curr.next
            # Reverse the link
            curr.next = prev
            # Move the previous and current pointers one step forward
            prev = curr
            curr = next_node

        # Return the new head
        return prev
    
# Time complexity: O(n) where n is the length of the linked list
# Space complexity: O(1) since we only use a constant amount of extra space