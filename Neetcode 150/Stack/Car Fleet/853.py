class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create a list of tuples, where each tuple contains the position and speed
        # of a car. The tuples are sorted in descending order of position.
        cars = sorted(zip(position, speed), reverse=True)

        # Initialize a variable to keep track of the number of fleets.
        fleets = 0

        # Initialize a variable to keep track of the time it takes for the slowest
        # car in the current fleet to reach the target.
        prev_time = float('inf')

        # Iterate over the cars in descending order of position.
        for pos, spd in cars:
            # Calculate the time it takes for the current car to reach the target.
            time = (target - pos) / spd

            # If the time is greater than the previous time, it means we have
            # encountered a new fleet of cars. Increment the number of fleets.
            if time > prev_time:
                fleets += 1
                prev_time = time

            # Update the previous time to the current time.
            prev_time = time

        # Return the number of fleets.
        return fleets

# time complexity: O(n log n), because sorting is O(n log n)
# space complexity: O(n), because we are using a list to store the cars