class TimeMap:
    def __init__(self):
        """
        Initialize a new TimeMap object.
        
        This function initializes a new TimeMap object. It does this by creating an empty dictionary 
        called 'store'. The 'store' dictionary is used to store key-value pairs, where the key is a string 
        representing a specific key and the value is a list of tuples. Each tuple in the list contains two 
        elements: an integer representing the timestamp and a string representing the value associated with 
        that timestamp.
        
        Parameters:
            None
        
        Returns:
            None
        """
        
        # Create an empty dictionary called 'store'
        self.store = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        Store a value for a given key at a specific timestamp.
        
        This function takes in a key, a value, and a timestamp as parameters. It stores the key-value pair in
        the 'store' dictionary. If the key does not exist in the dictionary, a new empty list is created for
        that key. The value is then appended to the list as a tuple, along with the timestamp.
        
        Parameters:
            key (str): The key for the value.
            value (str): The value to be stored.
            timestamp (int): The timestamp at which the value is stored.
        
        Returns:
            None
        """
        
        # Check if the key already exists in the 'store' dictionary
        if key not in self.store:
            # If the key does not exist, create a new empty list for that key
            self.store[key] = []
        
        # Append the value as a tuple with the timestamp to the list for the key
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        """
        Retrieve the value associated with a given key at a specific timestamp.
        
        This function takes in a key and a timestamp as parameters. It searches for the value associated with
        the key at the specified timestamp in the 'store' dictionary. If the key does not exist in the dictionary
        or if there is no value associated with the key at the specified timestamp, an empty string is returned.
        
        Parameters:
            key (str): The key for the value.
            timestamp (int): The timestamp at which the value is requested.
        
        Returns:
            str: The value associated with the key at the specified timestamp, or an empty string if the key does
                 not exist or if there is no value associated with the key at the specified timestamp.
        """
        
        # Check if the key exists in the 'store' dictionary
        if key not in self.store:
            # If the key does not exist, return an empty string
            return ""
        
        # Retrieve the list of values associated with the key from the 'store' dictionary
        values = self.store[key]
        
        # Initialize the left and right pointers for the binary search
        left = 0
        right = len(values) - 1
        
        # Perform binary search to find the value associated with the key at the specified timestamp
        while left <= right:
            # Calculate the middle index of the current search range
            mid = (left + right) // 2
            
            # Check if the timestamp of the value at the middle index is less than or equal to the specified timestamp
            if values[mid][0] <= timestamp:
                # If the timestamp is less than or equal to the specified timestamp, move the left pointer to the right of the middle index
                left = mid + 1
            else:
                # If the timestamp is greater than the specified timestamp, move the right pointer to the left of the middle index
                right = mid - 1
        
        # Check if there is a value associated with the key at the specified timestamp
        if right >= 0:
            # If there is a value, return the corresponding value
            return values[right][1]
        else:
            # If there is no value, return an empty string
            return ""
        
# Time complexity: 0(n log n) - Sorting is O(n log n)
# Space complexity: O(n) - We're using a list to store the values for each key.