class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        This function takes in a string s and an integer k, and returns the
        length of the longest substring in s that can be formed by no more
        than k occurrences of any character.
        """
        # Initialize an empty dictionary to keep track of the count of each
        # character in the substring
        char_count = {}
        
        # Initialize variables to keep track of the maximum length of the
        # substring and the maximum count of any character in the substring
        max_length = 0
        max_count = 0
        
        # Initialize variables to keep track of the start and end indices of
        # the current substring
        start = 0
        
        # Iterate through each character in the string
        for end in range(len(s)):
            # Increment the count of the current character in the dictionary
            char_count[s[end]] = char_count.get(s[end], 0) + 1
            
            # Update the maximum count to the maximum count of any character
            # in the substring
            max_count = max(max_count, char_count[s[end]])
            
            # If the length of the current substring minus the maximum count
            # of any character is greater than k, we can remove the character
            # at the start of the substring and move the start index forward
            if (end - start + 1) - max_count > k:
                char_count[s[start]] -= 1
                start += 1
            
            # Update the maximum length of the substring if the current length
            # is greater than the previous maximum length
            max_length = max(max_length, end - start + 1)
        
        # Return the maximum length of the substring
        return max_length

# Time Complexity: O(N)
# Space Complexity: O(1)