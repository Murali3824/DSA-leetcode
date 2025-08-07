class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        # subsets_count = 1 << n 
        # for num in range(subsets_count):
        #     subsets = []
        #     for i in range(n): 
        #         if num & (1 << i):
        #             subsets.append(nums[i])
        #     ans.append(subsets)
        # return ans

        def backtrack(start, path):
            ans.append(path[:])  # store a copy of the current path
            for i in range(start, len(nums)):
                path.append(nums[i])           # include nums[i]
                backtrack(i + 1, path)         # move to next index
                path.pop()                     # backtrack (remove last)

        backtrack(0, [])
        return ans