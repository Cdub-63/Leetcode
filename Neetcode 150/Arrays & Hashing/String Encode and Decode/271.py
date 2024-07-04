class Solution:
    def encode(self, strs: List[str]) -> str:
        # The encode function takes a list of strings as input and returns a string
        # that represents the encoded version of the input strings.
        
        # The encoded version of each string is formed by concatenating the length of the string
        # with a '#' character, followed by the string itself.
        
        # To encode each string, we iterate over the input list of strings. For each string,
        # we create a formatted string using an f-string. The f-string is formatted as follows:
        # "{length_of_string}#{string}". The length_of_string is the length of the current string,
        # and the string is the current string itself.
        
        # We then join all the formatted strings using the ''.join() method, which concatenates
        # all the strings in the list into a single string.
        
        # Finally, we return the encoded string.
        
        return ''.join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        # Initialize an empty list to store the decoded strings
        result = []
        # Initialize a variable to keep track of the current index in the string
        i = 0
        # Keep looping until we reach the end of the string
        while i < len(s):
            # Find the position of '#' by incrementing the index until we find '#'
            # Start searching from the current index
            j = i
            # Loop until we find '#'
            while s[j] != '#':
                # Move to the next character
                j += 1
            # Extract the length of the string by converting the substring from i to j to an integer
            # This is the number of characters between '#' and the start of the string
            length = int(s[i:j])
            # Extract the string itself by slicing the substring from j + 1 to j + 1 + length
            # This is the actual string we want to decode
            result.append(s[j + 1 : j + 1 + length])
            # Move to the next string by setting the current index to the end of the current string
            # This is the start of the next encoded string
            i = j + 1 + length
        
# time complexity: O(n), where n is the length of all strings
# space complexity: O(n), for encoded string