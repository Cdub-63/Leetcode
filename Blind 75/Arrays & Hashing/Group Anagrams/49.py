class Solution:
    # The solution uses the fact that anagrams are sorted versions of each other. 
    # This function groups the input strings based on their sorted versions.
    # For each string, the function takes the sorted version of the string as the key.
    # If a key is already in the dictionary, it appends the original string to the list of values.
    # Otherwise, it creates a new list with the original string as the only value.
    # Finally, it returns the list of values for each unique sorted string.
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {} # Initialize an empty dictionary to store the sorted strings and the original strings
        for s in strs: # Iterate over the input strings
            key = tuple(sorted(s)) # Take the sorted version of the string as the key
            d[key] = d.get(key, []) + [s] # If the key is already in the dictionary, append the original string to the list of values.
            # Otherwise, create a new list with the original string as the only value.
        return list(d.values()) # Return the list of values for each unique sorted string

# Time Complexity: O(NKlogK), where N is the number of strings, and K is the maximum length of a string.
# Space Complexity: O(NK), where N is the number of strings, and K is the maximum length of a string.