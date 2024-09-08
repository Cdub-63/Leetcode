class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Finds all combinations of candidates that sum up to the target.

        Args:
            candidates (List[int]): The list of numbers to choose from.
            target (int): The target sum.

        Returns:
            List[List[int]]: A list of combinations that sum up to the target.
        """
        res = []  # The result list to store the combinations

        def dfs(i, cur, total):
            """
            A helper function to do the depth-first search.

            Args:
                i (int): The current index in the candidates list.
                cur (List[int]): The current combination of numbers.
                total (int): The current total of the combination.
            """
            if total == target:
                # If the current total equals the target, add the current combination to the result list
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                # If we've reached the end of the list or the total exceeds the target, stop the search
                return

            cur.append(candidates[i])
            # Recursively call dfs to explore the combinations that include the current number
            dfs(i, cur, total + candidates[i])
            cur.pop()
            # And then call dfs again to explore the combinations that don't include the current number
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res
