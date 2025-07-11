class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def sum_values(d):
            sums = 0
            for i in nums:
                sums += ceil(i / d)
            return sums

        left, right = 1, max(nums)
        ans = 1
        while left <= right:
            mid = (left + right) // 2
            if sum_values(mid) <= threshold:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans 