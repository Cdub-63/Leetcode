class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        # two heaps, large, small, minheap, maxheap
        # heaps should be equal size
        self.small, self.large = [], []  # maxHeap, minHeap (python default)

    def addNum(self, num: int) -> None:
        """
        Add a new num to the data structure.

        The data structure is two heaps, a max heap (self.small) and a min heap (self.large).

        The max heap stores the smaller half of the numbers and is always 1 element larger than the min heap.
        The min heap stores the larger half of the numbers.

        The max heap is ordered such that the largest element is at the top, and the min heap is ordered such that the smallest element is at the top.

        The process works as follows:

        1. If the number is larger than the top element of the min heap, add it to the min heap.
        2. Otherwise, add it to the max heap.
        3. If the size of the max heap is now 2 elements larger than the size of the min heap, pop the top element from the max heap and add it to the min heap.
        4. If the size of the min heap is now 2 elements larger than the size of the max heap, pop the top element from the min heap and add it to the max heap.
        """
        if self.large and num > self.large[0]:
            # If the number is larger than the top element of the min heap, add it to the min heap.
            heapq.heappush(self.large, num)
        else:
            # Otherwise, add it to the max heap.
            heapq.heappush(self.small, -1 * num)

        if len(self.small) > len(self.large) + 1:
            # If the size of the max heap is now 2 elements larger than the size of the min heap, pop the top element from the max heap and add it to the min heap.
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            # If the size of the min heap is now 2 elements larger than the size of the max heap, pop the top element from the min heap and add it to the max heap.
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        """
        Find the median of the stream of numbers that have been added to the data structure.

        The median is the middle element of the sorted list of numbers. If the list has an even length,
        the median is the average of the two middle elements.

        If the size of the max heap (self.small) is greater than the size of the min heap (self.large),
        then the median is the top element of the max heap (i.e. the largest element in the smaller half).

        If the size of the min heap is greater than the size of the max heap, then the median is the top
        element of the min heap (i.e. the smallest element in the larger half).

        If the size of the max heap and the size of the min heap are equal, then the median is the average
        of the top element of the max heap and the top element of the min heap.
        """
        if len(self.small) > len(self.large):
            # The size of the max heap is greater than the size of the min heap.
            # The median is the top element of the max heap.
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            # The size of the min heap is greater than the size of the max heap.
            # The median is the top element of the min heap.
            return self.large[0]
        else:
            # The size of the max heap and the size of the min heap are equal.
            # The median is the average of the top element of the max heap and the top element of the min heap.
            return (-1 * self.small[0] + self.large[0]) / 2.0

# time complexity: O(log n)
# space complexity: O(n)