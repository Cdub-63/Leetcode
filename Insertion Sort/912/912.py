# Define a class for the solution
class Solution:
    # Define a method to sort an array of integers
    def sortArray(self, nums: List[int]) -> List[int]:
        # Define a helper function to merge two sorted subarrays
        def merge(arr, L, M, R):
            # Split the array into two subarrays
            left, right = arr[L:M+1], arr[M+1:R+1]
            i, j, k = L, 0, 0
            # Merge the subarrays back into the original array
            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1
            # If there are remaining elements in the left subarray, add them to the original array
            while j < len(left):
                nums[i] = left[j]
                j += 1
                i += 1
            # If there are remaining elements in the right subarray, add them to the original array
            while k < len(right):
                nums[i] = right[k]
                k += 1
                i += 1

        # Define a helper function to perform merge sort
        def mergeSort(arr, l, r):
            # If the array has one element, it is already sorted
            if l == r:
                return arr
            # Find the middle index of the array
            m = (l + r) // 2
            # Recursively sort the left and right halves of the array
            mergeSort(arr, l, m)
            mergeSort(arr, m + 1, r)
            # Merge the sorted halves back together
            merge(arr, l, m, r)
            return arr
        
        # Sort the input array and return it
        return mergeSort(nums, 0, len(nums) - 1)
    
# Time complexity: O(n log n)
# Space complexity: O(n)