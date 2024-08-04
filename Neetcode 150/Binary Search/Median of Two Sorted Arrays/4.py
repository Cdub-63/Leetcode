class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # If nums1 is larger than nums2, swap them to ensure nums1 is the smaller one
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        # Store the length of nums1 and nums2
        x, y = len(nums1), len(nums2)
        
        # Initialize the left and right pointers for the binary search
        low, high = 0, x

        # Perform binary search to find the median
        while low <= high:
            # Calculate the partition points for nums1 and nums2
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX

            # Calculate the maximum and minimum values for the left partition of nums1
            if partitionX == 0:
                maxLeftX = float('-inf')
            else:
                maxLeftX = nums1[partitionX - 1]
            if partitionX == x:
                minRightX = float('inf')
            else:
                minRightX = nums1[partitionX]
            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == x else nums1[partitionX]

            # Calculate the maximum and minimum values for the left partition of nums2
            if partitionY == 0:
                maxLeftY = float('-inf')
            else:
                maxLeftY = nums2[partitionY - 1]
            if partitionY == y:
                minRightY = float('inf')
            else:
                minRightY = nums2[partitionY]
            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == y else nums2[partitionY]

            # Check if the partitions of nums1 and nums2 have the desired property
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # If the total length of nums1 and nums2 is even, return the average of the two middle elements
                if (x + y) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                # If the total length of nums1 and nums2 is odd, return the maximum of the two middle elements
                else:
                    return max(maxLeftX, maxLeftY)
            # If the maximum element of the left partition of nums1 is greater than the minimum element of the right partition of nums2, move the left pointer to the left
            elif maxLeftX > minRightY:
                high = partitionX - 1
            # If the maximum element of the left partition of nums2 is greater than the minimum element of the right partition of nums1, move the right pointer to the right
            else:
                low = partitionX + 1

# Time complexity: O(log(min(m, n))), where m is the length of nums1 and n is the length of nums2
# Space complexity: O(1)