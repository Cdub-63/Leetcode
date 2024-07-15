class Solution:
    # This method calculates the product of all the elements in the input array except
    # for the current element. The result is stored in a new array and returned.
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Get the length of the input array
        n = len(nums)

        # Initialize an array to store the answer
        answer = [1] * n

        # Calculate the prefix products
        # Prefix product of i is the product of all the elements from 0 to i-1
        # This is done by multiplying the product so far with the current element
        prefix = 1
        for i in range(0, n):
            # Multiply the prefix product so far with the current element
            answer[i] = prefix
            prefix *= nums[i]

        # Calculate the postfix products
        # Postfix product of i is the product of all the elements from i+1 to the end
        # This is done by multiplying the product so far with the current element
        postfix = 1
        for i in range(n - 1, -1, -1):
            # Multiply the postfix product so far with the current element
            answer[i] *= postfix
            postfix *= nums[i]

        # Return the answer array containing the products of all the elements
        # except for the current element
        return answer

# time complexity: O(n), where n is the length of the input array
# space complexity: O(1)