class Solution:
    def isPalindrome(self, s: str) -> bool:
        # First, we create a new string by iterating over each character in the input string
        # If the character is either a letter or a number, we include it in the cleaned string
        # We also convert the character to lowercase using the .lower() method, which is necessary
        # because we want to treat 'A' and 'a' as the same character when checking for palindromes
        # We use the .isalnum() method to check if a character is either a letter or a number
        cleaned = ''.join(char.lower() for char in s if char.isalnum())

        # Next, we check if the cleaned string is equal to its reverse.
        # The [::-1] syntax is a way to access the characters in a string in reverse order
        return cleaned == cleaned[::-1]

# time complexity: O(n), where n is the length of the input string
# space complexity: O(n), because we are using a new string to store the cleaned string