class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        count = {0: 1}  # prefix_sum -> frequency
        curr_sum = 0
        result = 0
        
        for num in nums:
            curr_sum += num
            if (curr_sum - goal) in count:
                result += count[curr_sum - goal]
            count[curr_sum] = count.get(curr_sum, 0) + 1
        
        return result
