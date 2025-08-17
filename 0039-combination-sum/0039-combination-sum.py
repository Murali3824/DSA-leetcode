class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(index, path, current_sum):
            if current_sum == target:
                result.append(path[:])
                return
            if current_sum > target or index == len(candidates):
                return

            # Include current element
            path.append(candidates[index])
            current_sum += candidates[index]   # add before recursive call
            backtrack(index, path, current_sum)
            current_sum -= candidates[index]   # subtract while backtracking
            path.pop()                         # backtrack

            # Exclude current element
            backtrack(index + 1, path, current_sum)

        backtrack(0, [], 0)
        return result