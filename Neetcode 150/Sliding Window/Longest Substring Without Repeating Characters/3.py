class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        This function finds the length of the longest substring in a given string
        that does not contain any repeating characters. It does this by using a
        hashmap to keep track of the index of each character in the substring.
        It loops through each character in the string and checks if it has already
        been seen in the substring. If it has, it updates the start index of the
        substring to be right after the last occurrence of the character. If it has
        not been seen before, it updates the hashmap with the character as a key
        and the current index as a value. It then updates the maximum length of
        the substring if the current length is greater than the previous maximum.
        The function returns the maximum length of the substring.
        """

        # Create a hashmap to store the index of each character
        char_index = {}

        # Initialize the maximum length of the substring to 0
        max_length = 0

        # Initialize the start index of the substring to 0
        start = 0

        # Loop through each character in the string
        for end, char in enumerate(s):
            # If the character has already been seen in the substring
            if char in char_index and char_index[char] >= start:
                # Update the start index to be right after the last occurrence of the character
                start = char_index[char] + 1
            else:
                # Update the maximum length of the substring if the current length is greater than the previous maximum
                max_length = max(max_length, end - start + 1)

            # Update the hashmap with the character as a key and the current index as a value
            char_index[char] = end

        # Return the maximum length of the substring
        return max_length

# Time Complexity: O(N), where N is the length of the input string.
# Space Complexity: O(N), worse case where all characters in the string are unique.