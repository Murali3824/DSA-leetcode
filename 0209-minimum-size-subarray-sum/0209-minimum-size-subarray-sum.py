class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, sub_sum, min_len = 0, 0, float('inf')
        for right in range(len(nums)):
            sub_sum += nums[right]
            while sub_sum >= target:
                min_len = min(min_len, right - left + 1)
                sub_sum -= nums[left]
                left += 1
        return 0 if min_len == float('inf') else min_len
        