class Solution:
def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize two pointers, one at the beginning and one at the end of the numbers list
        left = 0
        right = len(numbers) - 1

        # Continue looping until the two pointers meet
        while left < right:
            # Calculate the sum of the values at the left and right pointers
            curSum = numbers[left] + numbers[right]

            # If the current sum matches the target, return the indices (adjusted for 1-based indexing)
            if curSum == target:
                return [left + 1, right + 1]
            # If the current sum is less than the target, move the left pointer to the right to increase the sum
            elif curSum < target:
                left += 1
            # If the current sum is greater than the target, move the right pointer to the left to decrease the sum
            else:
                right -= 1

        # If no two numbers sum up to the target, return an empty list
        return []

# Time Complexity: O(n)
# Space Complexity: O(1)