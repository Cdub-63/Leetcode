class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        """
        The constructor for the KthLargest class.

        Args:
            k (int): The number of elements to keep track of.
            nums (List[int]): The list of numbers to initialize the heap with.

        """
        # Create a minHeap to store the K largest integers
        self.minHeap = nums
        self.k = k

        # Heapify the list of numbers to make it a valid minHeap
        heapq.heapify(self.minHeap)

        # If the list has more than K elements, remove the smallest elements
        # until the length of the list is equal to K
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        """
        Adds a new element to the minHeap and returns the kth largest element.

        The process works as follows:

        1. Push the new element onto the minHeap using heapq.heappush.
        2. If the length of the minHeap is now greater than k, pop the smallest
           element from the minHeap using heapq.heappop. This ensures that the
           minHeap always has exactly k elements, and the smallest element is
           always the kth largest element.

        The kth largest element is then returned as the result of the function.

        """
        # Push the new element onto the minHeap
        heapq.heappush(self.minHeap, val)

        # If the length of the minHeap is now greater than k, pop the smallest
        # element from the minHeap
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        # The kth largest element is now at the root of the minHeap, so return it
        return self.minHeap[0]

# Time complexity: O(n log k), where n is the length of the input list nums. This is because the heapify operation takes O(n log k) time.
# Space complexity is O(k), where k is the number of elements to keep track of. This is because the algorithm uses a min-heap to store the k largest elements.