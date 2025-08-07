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
            ans.append(path)
            for i in range(start, n):
                backtrack(i + 1, path + [nums[i]])
                
        backtrack(0, [])
        return ans