# Solution: Sorting
# Time Complexity:
#   - Best Case: O(n)
#   - Average Case: O(n*log(n))
#   - Worst Case:O(n*log(n))
# Extra Space Complexity: O(n)
class Solution1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Finds the kth largest element in the given list of numbers.

        Args:
            nums (List[int]): The list of numbers to search through.
            k (int): The 1-indexed position of the element to find.

        Returns:
            int: The kth largest element.
        """
        # First, sort the list of numbers. This has a time complexity of O(n*log(n))
        nums.sort()
        # Then, return the kth element from the end of the list. The indexing is 0-based, so subtract 1 from k.
        return nums[len(nums) - k]


# Solution: QuickSelect
# Time Complexity:
#   - Best Case: O(n)
#   - Average Case: O(n)
#   - Worst Case: O(n^2)
# Extra Space Complexity: O(1)
class Solution2:
    def partition(self, nums: List[int], left: int, right: int) -> int:
        """
        Partitions the given list of numbers around a pivot element.

        The pivot element is chosen as the element at the rightmost index of the given sublist.
        All elements in the sublist that are less than the pivot are swapped to the left of the pivot,
        and all elements greater than the pivot are swapped to the right.
        The index of the pivot element is returned.

        Args:
            nums (List[int]): The list of numbers to partition.
            left (int): The leftmost index of the sublist to partition.
            right (int): The rightmost index of the sublist to partition.

        Returns:
            int: The 0-indexed position of the pivot element after partitioning.
        """
        # Choose the pivot element as the element at the rightmost index of the sublist.
        pivot = nums[right]

        # Keep track of the index where the next element smaller than the pivot should go.
        # This index starts at the leftmost index of the sublist.
        fill = left

        # Iterate over the sublist from the leftmost index to the rightmost index.
        for i in range(left, right):
            # If the current element is less than or equal to the pivot...
            if nums[i] <= pivot:
                # Swap it with the element at the `fill` index.
                nums[fill], nums[i] = nums[i], nums[fill]

                # Increment the `fill` index to keep track of the new position of the pivot.
                fill += 1

        # Swap the pivot element with the element at the `fill` index.
        nums[fill], nums[right] = nums[right], nums[fill]

        # Return the 0-indexed position of the pivot element after partitioning.
        return fill

    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Finds the kth largest element in the given list of numbers.

        Args:
            nums (List[int]): The list of numbers to search through.
            k (int): The 1-indexed position of the element to find.

        Returns:
            int: The kth largest element.
        """
        # Convert the kth largest element to a 0-indexed position.
        k = len(nums) - k

        # Set the left and right bounds of the search space.
        left, right = 0, len(nums) - 1

        # Keep searching until we find the kth largest element.
        while left < right:
            # Partition the search space around a pivot element.
            pivot = self.partition(nums, left, right)

            # If the pivot element is less than the kth element, move the left
            # bound to the right of the pivot element.
            if pivot < k:
                left = pivot + 1
            # If the pivot element is greater than the kth element, move the
            # right bound to the left of the pivot element.
            elif pivot > k:
                right = pivot - 1
            # If the pivot element is the kth element, we have found the
            # element, so break out of the loop.
            else:
                break

        # Return the kth largest element.
        return nums[k]
