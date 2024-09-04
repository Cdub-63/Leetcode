class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        This function takes a list of tasks and an integer n, and returns the minimum time
        required to complete all tasks given the constraint that two tasks of the same type
        must be separated by at least n intervals.

        The time complexity of this algorithm is O(N), where N is the length of the tasks list.
        The space complexity is O(N), where N is the length of the tasks list.
        """
        # Count the occurrences of each task in the list
        count = Counter(tasks)
        # Create a max heap of the counts
        maxHeap = [-cnt for cnt in count.values()]
        # Heapify the max heap
        heapq.heapify(maxHeap)
        # Initialize time and queue
        time = 0
        q = deque()  # pairs of [-cnt, idleTime]
        while maxHeap or q:
            # Increase time by 1
            time += 1
            # If the max heap is empty, then all tasks have been completed, so
            # just return the current time
            if not maxHeap:
                time = q[0][1]
            # Otherwise, pop the top element from the max heap and decrease
            # the count by 1
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                # If the count is not 0, then add it back to the queue with the
                # current time + n as the idle time
                if cnt:
                    q.append([cnt, time + n])
            # If the queue is not empty and the idle time of the first element
            # in the queue is equal to the current time, then pop the first
            # element from the queue and add it back to the max heap
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        # Return the minimum time required to complete all tasks
        return time


# Greedy algorithm
class Solution(object):
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Given a list of tasks and an integer n, return the minimum time required to complete all tasks given the constraint that two tasks of the same type must be separated by at least n intervals.

        The time complexity of this algorithm is O(N), where N is the length of the tasks list.
        The space complexity is O(N), where N is the length of the tasks list.
        """
        # Count the occurrences of each task in the list
        counter = collections.Counter(tasks)
        
        # Find the maximum count of any task
        max_count = max(counter.values())
        
        # Calculate the minimum time required to complete all tasks
        # It is the maximum count subtracted by 1 (because we don't need to idle
        # after the last task), multiplied by the number of intervals we need
        # to wait between two tasks of the same type plus 1 (because we need
        # to idle for one interval after the last task), plus the number of
        # tasks that have the maximum count
        min_time = (max_count - 1) * (n + 1) + \
                    sum(map(lambda count: count == max_count, counter.values()))
        
        # The minimum time required is the maximum of the minimum time and the
        # length of the tasks list
        return max(min_time, len(tasks))

# Time complexity: O(N)
# Space complexity: O(N)