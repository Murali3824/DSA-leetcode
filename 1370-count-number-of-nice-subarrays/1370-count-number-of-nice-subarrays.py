class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atmost(k):
            left = 0
            result = 0
            count = 0
            
            for right in range(len(nums)):
                if nums[right] % 2 == 1:
                    k -= 1
                while k < 0:
                    if nums[left] % 2 == 1:
                        k += 1
                    left += 1
                result += right - left + 1
            return result

        return atmost(k) - atmost(k-1)