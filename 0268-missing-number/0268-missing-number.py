class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum1 = 0
        sum2 = 0
        n = len(nums)
        for i in range(n):
            sum1 = sum1 + nums[i]
        sum2 = (n*(n+1))//2
        return (sum2 - sum1)
            
        