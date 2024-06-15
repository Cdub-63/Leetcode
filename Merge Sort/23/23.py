# Define a class for the solution
class Solution:    
    # Define a method to merge k sorted linked lists
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # If the input list is empty, return None
        if not lists or len(lists) == 0:
            return None
        
        # While there is more than one list in the input list
        while len(lists) > 1:
            # Initialize an empty list to store the merged lists
            mergedLists = []
            # Iterate over the input list two at a time
            for i in range(0, len(lists), 2):
                # Get the two lists to merge
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                # Merge the two lists and add the result to the list of merged lists
                mergedLists.append(self.mergeList(l1, l2))
            # Replace the input list with the list of merged lists
            lists = mergedLists
        # Return the single list in the input list
        return lists[0]
    
    # Define a method to merge two sorted linked lists
    def mergeList(self, l1, l2):
        # Create a dummy node to serve as the head of the merged list
        dummy = ListNode()
        # Initialize a pointer to the tail of the merged list
        tail = dummy

        # While both input lists have nodes
        while l1 and l2:
            # If the value of the first node of l1 is smaller
            if l1.val < l2.val:
                # Add it to the merged list
                tail.next = l1
                # Move to the next node in l1
                l1 = l1.next
            else:
                # Otherwise, add the first node of l2 to the merged list
                tail.next = l2
                # Move to the next node in l2
                l2 = l2.next
            # Move to the next node in the merged list
            tail = tail.next
        # If there are remaining nodes in l1, add them to the merged list
        if l1:
            tail.next = l1
        # If there are remaining nodes in l2, add them to the merged list
        if l2:
            tail.next = l2
        # Return the merged list, skipping the dummy node
        return dummy.next

# Time complexity: O(nlogk) where n is the total number of nodes in the input lists and k is the number of lists
# Space complexity: O(1) as we are not using any extra space