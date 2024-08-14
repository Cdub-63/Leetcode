class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        This function merges k sorted linked lists into one sorted linked list.

        Args:
            lists (List[ListNode]): A list of k sorted linked lists.

        Returns:
            ListNode: A single sorted linked list which contains all the elements from the input lists.
        """
        # If the input list is empty or has only one element, return None.
        if not lists or len(lists) == 0:
            return None

        # While there is more than one list in the input list,
        # merge the two lists and update the input list.
        while len(lists) > 1:
            # Initialize an empty list to store the merged lists.
            mergedLists = []

            # Iterate over the input list two at a time.
            for i in range(0, len(lists), 2):
                # Get the two lists to merge.
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None

                # Merge the two lists and add the result to the list of merged lists.
                mergedLists.append(self.mergeList(l1, l2))

            # Replace the input list with the list of merged lists.
            lists = mergedLists

        # Return the single list in the input list.
        return lists[0]

    def mergeList(self, l1, l2):
        # Create a new dummy node to act as the head of the merged list.
        # This dummy node will be discarded later to return the actual head of the merged list.
        dummy = ListNode()
        # Initialize a pointer to the tail of the merged list, which will point to the last node in the list.
        # This is necessary for appending nodes to the list.
        tail = dummy

        # Loop until both input lists have no more nodes.
        while l1 and l2:
            # Compare the values of the first nodes in the input lists.
            if l1.val < l2.val:
                # If the value in the first node of l1 is smaller,
                # append the node from l1 to the merged list.
                tail.next = l1
                # Move the pointer to the next node in l1.
                l1 = l1.next
            else:
                # If the value in the first node of l2 is smaller or equal,
                # append the node from l2 to the merged list.
                tail.next = l2
                # Move the pointer to the next node in l2.
                l2 = l2.next
            # Move the tail pointer to the next node in the merged list.
            tail = tail.next

        # Append the remaining nodes from l1 (if any) to the merged list.
        while l1:
            tail.next = l1
            l1 = l1.next
            tail = tail.next

        # Append the remaining nodes from l2 (if any) to the merged list.
        while l2:
            tail.next = l2
            l2 = l2.next
            tail = tail.next

        # Return the head of the merged list by discarding the dummy node.
        return dummy.next

# Time Complexity: O(n log k) where n is the total number of nodes in all the lists and k is the number of lists.
# Space Complexity: O(1)