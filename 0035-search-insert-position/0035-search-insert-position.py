class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # LOWERBOUND
        ans = len(nums)
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                ans = mid
                right = mid
            else:
                left = mid + 1
        return ans

                    

        