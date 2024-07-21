class Solution:
def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Edge case: if the input list is empty or window size is 0, return an empty list
        if not nums or k == 0:
            return []

        result = []  # Initialize an empty list to store the maximum values in the sliding window
        queue = deque()  # Initialize a deque to store the indices of elements in the sliding window

        for i, num in enumerate(nums):
            # Remove elements from the front of the deque if they are outside the current window
            if queue and queue[0] == i - k:
                queue.popleft()

            # Remove elements from the back of the deque if they are smaller than the current element
            while queue and nums[queue[-1]] < num:
                queue.pop()

            # Add the current index to the deque
            queue.append(i)

            # If we have processed at least k elements, add the maximum element to the result list
            if i >= k - 1:
                result.append(nums[queue[0]])

        return result


# time complexity: O(n), where n is the number of elements in the input list
# space complexity: O(k), where k is the size of the sliding window