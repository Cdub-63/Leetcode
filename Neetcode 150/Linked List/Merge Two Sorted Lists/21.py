class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to start our merged list. This node will be skipped
        # when returning the final merged list.
        dummy = ListNode(0)
        
        # We'll use a pointer to keep track of the node we're currently adding to in the merged list.
        current = dummy
        
        # We'll continue looping until we've exhausted both input lists.
        while list1 and list2:
            # Compare the values of the nodes at the heads of each list. Whichever one is smaller,
            # we'll add to the merged list and advance the pointer to the next node in that list.
            if list1.val <= list2.val:
                # Add the smaller node to the merged list.
                current.next = list1
                # Move the pointer to the next node in the list.
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            # Move the pointer to the next node in the merged list.
            current = current.next
        
        # If there are remaining nodes in either list, add them to the merged list.
        if list1:
            # Add the remaining nodes from list1 to the merged list.
            current.next = list1
        if list2:
            # Add the remaining nodes from list2 to the merged list.
            current.next = list2
        
        # Return the head of the merged list (skip the dummy node).
        return dummy.next

# Time Complexity: O(n + m) where n and m are the lengths of list1 and list2
# Space Complexity: O(1)