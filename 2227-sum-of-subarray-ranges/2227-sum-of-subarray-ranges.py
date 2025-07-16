class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        total = 0
        for i in range(len(nums)):
            subarray = []
            for j in range(i,len(nums)):
                subarray.append(nums[j])
                total += (max(subarray) - min(subarray))
        return total