# Define a class for the solution
class Solution:
    # Define a method to count the number of students unable to eat lunch
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # Initialize the result as the total number of students
        res = len(students)
        # Count the number of students who prefer each type of sandwich
        cnt = Counter(students)

        # Iterate over the sandwiches in the stack
        for sandwich in sandwiches:
            # If there are students who prefer the current sandwich
            if cnt[sandwich] > 0:
                # Decrease the number of students unable to eat lunch
                res -= 1
                # Decrease the number of students who prefer the current sandwich
                cnt[sandwich] -= 1
            else:
                # If no students prefer the current sandwich, return the result
                return res

        # Return the result
        return res

# Time complexity: O(n), where n is the number of students
# Space complexity: O(n), where n is the number of students