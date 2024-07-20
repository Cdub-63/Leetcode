class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # If the length of s1 is greater than the length of s2, it is impossible to find a permutation of s1 in s2
        if len(s1) > len(s2):
            return False

        # Create a frequency dictionary for s1
        s1_freq = {}
        # Create a frequency dictionary for the current window of s2
        window_freq = {}

        # Populate s1_freq with the frequency of each character in s1
        for char in s1:
            s1_freq[char] = s1_freq.get(char, 0) + 1

        # Populate window_freq with the frequency of each character in the first window of s2
        for i in range(len(s1)):
            window_freq[s2[i]] = window_freq.get(s2[i], 0) + 1

        # If the frequency dictionaries are equal, a permutation of s1 is found in s2
        if s1_freq == window_freq:
            return True

        # Iterate over the rest of s2, expanding the window and checking for a permutation of s1
        for i in range(len(s1), len(s2)):
            # Decrement the frequency of the character leaving the window
            window_freq[s2[i - len(s1)]] -= 1
            # If the frequency of the character leaving the window becomes 0, remove it from the dictionary
            if window_freq[s2[i - len(s1)]] == 0:
                del window_freq[s2[i - len(s1)]]

            # Increment the frequency of the character entering the window
            window_freq[s2[i]] = window_freq.get(s2[i], 0) + 1

            # If the frequency dictionaries are equal, a permutation of s1 is found in s2
            if s1_freq == window_freq:
                return True

        # If no permutation of s1 is found in s2, return False
        return False

# time complexity: O(n), where n is the number of characters in s2
# space complexity: O(k), where k is the number of unique characters in s1