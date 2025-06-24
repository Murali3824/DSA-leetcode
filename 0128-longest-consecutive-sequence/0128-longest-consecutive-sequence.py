class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 1
        max_count = 1
        nums.sort()
        if len(nums) == 0:
            return 0
        for i in range(1,len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            if nums[i] == nums[i-1]+1:
                count += 1
                max_count = max(max_count,count)
            else:
                count = 1
        return max_count
            
        