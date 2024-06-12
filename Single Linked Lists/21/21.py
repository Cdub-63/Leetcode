# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Iterative solution
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Create a dummy node
        dummy = node = ListNode()

        # Iterate while both lists have nodes
        while list1 and list2:
            # If the value of list1's node is smaller
            if list1.val < list2.val:
                # Add it to the merged list
                node.next = list1
                # Move to the next node in list1
                list1 = list1.next
            else:
                # Otherwise, add the node from list2
                node.next = list2
                # Move to the next node in list2
                list2 = list2.next
            # Move to the next node in the merged list
            node = node.next

        # Add the remaining nodes from either list1 or list2
        node.next = list1 or list2

        # Return the merged list, skipping the dummy node
        return dummy.next

# Recursive solution
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # If list1 is empty, return list2
        if not list1:
            return list2
        # If list2 is empty, return list1
        if not list2:
            return list1
        # Determine which list has the smaller head
        lil, big = (list1, list2) if list1.val < list2.val else (list2, list1)
        # Recursively merge the rest of the lists
        lil.next = self.mergeTwoLists(lil.next, big)
        # Return the merged list
        return lil
    
# Iterative Time complexity: O(n + m) where n and m are the lengths of list1 and list2
# Iterative Space complexity: O(1)
# Recursive Time complexity: O(n + m) where n and m are the lengths of list1 and list2
# Recursive Space complexity: O(n + m) where n and m are the lengths of list1 and list2