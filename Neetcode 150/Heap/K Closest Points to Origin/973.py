class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        This function takes a list of points and an integer k, and returns the k points closest to the origin (0, 0)
        
        """
        # Create a minHeap to store the points and their distances to the origin
        minHeap = []
        for x, y in points:
            # Calculate the distance from the origin to the point
            dist = (x ** 2) + (y ** 2)
            # Store the distance and the point in the minHeap
            minHeap.append((dist, x, y))
        
        # Heapify the minHeap to ensure that it is a valid minHeap
        heapq.heapify(minHeap)
        # Initialize a list to store the k closest points
        res = []
        # Pop the k smallest distances from the minHeap and add the points to the result list
        for _ in range(k):
            # The _ variable is a throwaway variable, and is used to ignore the value returned by the heappop function
            _, x, y = heapq.heappop(minHeap)
            # Add the point to the result list
            res.append((x, y))
        # Return the result list
        return res

# time complexity: O(n log k)
# space complexity: O(n)