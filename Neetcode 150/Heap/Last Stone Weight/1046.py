class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Negate all of the stones, because Python's heapq is a min-heap
        # and we want a max-heap.
        stones = [-s for s in stones]

        # Heapify the list of stones into a max-heap.
        heapq.heapify(stones)

        # While there is more than one stone in the heap...
        while len(stones) > 1:
            # Pop the two heaviest stones off the heap.
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            # If the second stone is heavier than the first stone, then
            # there is leftover weight from the second stone, so we push it
            # back onto the heap.
            if second > first:
                heapq.heappush(stones, first - second)

        # At this point, there is only one stone left in the heap, or else
        # the heap is empty.

        # If the heap is empty, then the weight of the last stone is 0.
        # Otherwise, the weight of the last stone is the negation of the
        # only element in the heap (because we negated all of the elements
        # when we built the heap).
        stones.append(0)
        return abs(stones[0])

# Time complexity: O(n log n)
# space complexity: O(n)