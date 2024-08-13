class Node:
    def __init__(self, key=0, value=0):
        """
        Initialize a new Node object with the given key-value pair.
        
        This function initializes a new Node object with the given key and value.
        The Node object will have four attributes:
        - key: an integer representing the key of the node
        - value: an integer representing the value of the node
        - prev: a reference to the previous node in the linked list, or None if it is the head node
        - next: a reference to the next node in the linked list, or None if it is the tail node
        
        Parameters:
            key (int): The key of the Node. Default is 0.
            value (int): The value of the Node. Default is 0.
        """
        
        # Assign the given key to the Node's key attribute
        self.key = key
        
        # Assign the given value to the Node's value attribute
        self.value = value
        
        # Initialize the previous node reference of the Node as None
        # This is used to link the Node to the previous node in the linked list
        self.prev = None
        
        # Initialize the next node reference of the Node as None
        # This is used to link the Node to the next node in the linked list
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        """
        Initialize a new LRUCache object with the given capacity.

        This function initializes a new LRUCache object with the given capacity. 
        The LRUCache object will have three attributes:
        - cache: a dictionary to store the key-value pairs
        - capacity: an integer representing the maximum number of key-value pairs the cache can hold
        - head: a Node object representing the head of the doubly linked list
        - tail: a Node object representing the tail of the doubly linked list

        Parameters:
            capacity (int): The maximum number of key-value pairs the cache can hold.
        """
        
        # Initialize an empty dictionary to store the key-value pairs
        self.cache = {}
        
        # Assign the given capacity to the LRUCache's capacity attribute
        self.capacity = capacity
        
        # Initialize the head and tail nodes of the doubly linked list
        # The head node has no previous node, and the tail node has no next node
        # The head node is used as a sentinel node to simplify the implementation
        self.head = Node()
        self.tail = Node()
        
        # Set the next attribute of the head node to point to the tail node
        # This makes the head node the first node in the linked list
        # The previous attribute of the head node is not used, so it is left as None
        self.head.next = self.tail
        
        # Set the previous attribute of the tail node to point to the head node
        # This makes the tail node the last node in the linked list
        # The next attribute of the tail node is not used, so it is left as None
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        """
        Retrieves the value associated with the given key from the cache.
        
        If the key exists in the cache, this function removes the corresponding node from its current position
        in the linked list and adds it to the end of the linked list (bringing it to the front). It then returns
        the value of the node. If the key does not exist in the cache, this function returns -1.
        
        Parameters:
            key (int): The key to retrieve from the cache.
        
        Returns:
            int: The value associated with the key, or -1 if the key does not exist in the cache.
        """
        
        # Check if the key exists in the cache
        if key in self.cache:
            # If the key exists, retrieve the corresponding node from the cache
            node = self.cache[key]
            
            # Remove the node from its current position in the linked list
            self._remove(node)
            
            # Add the node to the end of the linked list (bringing it to the front)
            self._add(node)
            
            # Return the value of the node
            return node.value
        
        # If the key does not exist in the cache, return -1
        return -1

    def put(self, key: int, value: int) -> None:
        # If the key already exists in the cache, remove the corresponding node from its current position
        # in the linked list and add it to the end of the linked list (bringing it to the front).
        # Then, update the value of the node and add it to the cache.
        # If the cache is full, remove the least recently used node from the cache and the linked list.
        
        # Check if the key exists in the cache
        if key in self.cache:
            # If the key exists, retrieve the corresponding node from the cache
            node = self.cache[key]
            
            # Remove the node from its current position in the linked list
            self._remove(node)
            
            # Update the value of the node
            node.value = value
            
            # Add the node to the end of the linked list (bringing it to the front)
            self._add(node)
        else:
            # If the key does not exist in the cache, create a new node with the key and value
            node = Node(key, value)
            
            # Add the node to the end of the linked list (bringing it to the front)
            self._add(node)
            
            # Add the node to the cache
            self.cache[key] = node
            
            # Check if the cache is full
            if len(self.cache) > self.capacity:
                # If the cache is full, remove the least recently used node from the cache and the linked list
                
                # Retrieve the least recently used node from the head of the linked list
                lru = self.head.next
                
                # Remove the least recently used node from the linked list
                self._remove(lru)
                
                # Remove the least recently used node from the cache
                del self.cache[lru.key]

    def _remove(self, node):
        # The 'node' parameter represents a node in the linked list.
        
        # To remove the node from the linked list, we need to update the 'next' and 'prev' pointers of
        # the nodes before and after the node to be removed.
        
        # Step 1: Update the 'next' pointer of the node before the node to be removed.
        # Set the 'next' pointer of the node before the node to be removed to the node after the node to be removed.
        # This effectively skips over the node to be removed in the linked list.
        node.prev.next = node.next
        
        # Step 2: Update the 'prev' pointer of the node after the node to be removed.
        # Set the 'prev' pointer of the node after the node to be removed to the node before the node to be removed.
        # This effectively skips over the node to be removed in the linked list.
        node.next.prev = node.prev

    def _add(self, node):
        # Set the 'prev' attribute of the 'node' parameter to the 'prev' attribute of the tail's previous node.
        # This sets the 'prev' pointer of the new node to point to the node that was previously the tail's previous node.
        node.prev = self.tail.prev
        
        # Set the 'next' attribute of the 'node' parameter to the 'next' attribute of the tail node.
        # This sets the 'next' pointer of the new node to point to the tail node.
        node.next = self.tail
        
        # Set the 'next' attribute of the tail's previous node to the 'next' attribute of the 'node' parameter.
        # This updates the 'next' pointer of the node that was previously the tail's previous node to point to the new node.
        self.tail.prev.next = node
        
        # Set the 'prev' attribute of the tail node to the 'prev' attribute of the 'node' parameter.
        # This updates the 'prev' pointer of the tail node to point to the new node.
        self.tail.prev = node

# Time Complexity: O(1)
# Space Complexity: O(capacity)