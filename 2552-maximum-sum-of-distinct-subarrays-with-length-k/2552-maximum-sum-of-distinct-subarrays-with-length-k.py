class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        curr_cum = 0
        max_sum = 0
        seen = set()
    
        for right in range(len(nums)):
            
            # shrink if duplicate appears
            while nums[right] in seen:
                seen.remove(nums[left])
                curr_cum -= nums[left]
                left += 1
        
            # add current element
            curr_cum += nums[right]
            seen.add(nums[right])
        
        
            # shrink if window > k
            if right - left + 1 > k:
                seen.remove(nums[left])
                curr_cum -= nums[left]
                left += 1
        
            # valid window of size k
            if right - left + 1 == k:
                max_sum = max(max_sum, curr_cum)
        
        return max_sum
