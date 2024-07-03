class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each number
        # Create an empty dictionary to store the count of each number
        count = {}
        # Iterate over each number in the input list
        for num in nums:
            # If the number is already in the dictionary, increment its count
            if num in count:
                count[num] += 1
            # If the number is not in the dictionary, add it with a count of 1
            else:
                count[num] = 1
        
        # Step 2: Create a list of unique numbers
        # Convert the keys of the count dictionary into a list
        unique = list(count.keys())
        
        # Step 3: Sort the unique numbers based on their frequency
        # Define a helper function to get the frequency of a number
        def get_freq(num):
            # Return the count of the given number
            return count[num]
        
        # Sort the unique numbers in descending order of their frequency
        # The sorted() function returns a new list, so we assign the result back to unique
        unique = sorted(unique, key=get_freq, reverse=True)
        
        # Step 4: Return the k most frequent elements
        # Return the first k elements of the sorted list of unique numbers
        return unique[:k]
    
# Time Complexity: O(n log(n)), because sorting is O(n log(n))
# Space Complexity: O(n), because we are using a dictionary to store the frequency of each number