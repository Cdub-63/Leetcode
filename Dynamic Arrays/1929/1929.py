# Define a class for the solution
class Solution:
    # Define a method to concatenate the array with itself
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Initialize an empty list for the result
        ans = []
        # Repeat the process twice to concatenate the array with itself
        for i in range(2):
            # Iterate over the input array
            for n in nums:
                # Append each element to the result list
                ans.append(n)
        # Return the result list
        return ans

# Time complexity: O(n), where n is the length of the input array
# Space complexity: O(n), where n is the length of the input array