class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the input list to ensure that the numbers are in ascending order
        nums.sort()
        
        # Initialize an empty list to store the resulting triplets
        result = []
        
        # Get the length of the input list
        n = len(nums)
        
        # Iterate over the input list, starting from the second-to-last element
        for i in range(n - 2):
            # If the current element is the same as the previous element, skip it
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Initialize pointers for the left and right ends of the list
            left, right = i + 1, n - 1
            
            # While the left pointer is less than the right pointer
            while left < right:
                # Calculate the sum of the current element, the element at the left pointer, and the element at the right pointer
                sum = nums[i] + nums[left] + nums[right]
                
                # If the sum is equal to zero
                if sum == 0:
                    # Append the current triplet to the result list
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicate elements on the left side
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    
                    # Skip duplicate elements on the right side
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move the left and right pointers to the next valid positions
                    left += 1
                    right -= 1
                    
                # If the sum is less than zero, move the left pointer to the right
                elif sum < 0:
                    left += 1
                    
                # If the sum is greater than zero, move the right pointer to the left
                else:
                    right -= 1
                    
        # Return the resulting list of triplets
        return result

# Time Complexity: O(n^2), because we have two nested loops
# Space Complexity: O(n), because we use an additional list to store the triplets