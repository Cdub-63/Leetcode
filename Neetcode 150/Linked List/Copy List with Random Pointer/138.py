class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Check if the input linked list is empty
        if not head:
            return None
        
        # Step 1: Create a dictionary to store the mapping of old nodes to new nodes
        # This dictionary will be used to keep track of the newly created nodes
        # and their corresponding relationships with the old nodes
        old_to_new = {}
        
        # First pass: create new nodes
        # Traverse the input linked list and create new nodes for each node in the list
        curr = head
        while curr:
            # Create a new node with the same value as the current node
            new_node = Node(curr.val)
            # Store the mapping of the current node to the new node
            old_to_new[curr] = new_node
            # Move to the next node in the input linked list
            curr = curr.next
        
        # Second pass: connect new nodes
        # Traverse the input linked list again and connect the new nodes accordingly
        curr = head
        while curr:
            # Get the new node corresponding to the current node
            new_node = old_to_new[curr]
            # Connect the new node's next pointer to the new node corresponding to the next node in the input linked list
            new_node.next = old_to_new.get(curr.next)
            # Connect the new node's random pointer to the new node corresponding to the random node in the input linked list
            new_node.random = old_to_new.get(curr.random)
            # Move to the next node in the input linked list
            curr = curr.next
        
        # Return the new node corresponding to the head of the input linked list
        return old_to_new[head]

# Time Complexity: O(N)
# Space Complexity: O(N)