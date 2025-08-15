class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, s, size = 0, 0, float('inf')
        for r in range(len(nums)):
            s += nums[r]
            while s >= target:
                size = min(size, r - l + 1)
                s -= nums[l]
                l += 1
        return 0 if size == float('inf') else size


        # start = 0
        # current_sum = 0
        # min_len = float('inf')

        # for end in range(len(nums)):
        #     current_sum += nums[end]

        #     while current_sum >= target:
        #         min_len = min(min_len, end - start + 1)
        #         current_sum -= nums[start]
        #         start += 1

        # return min_len if min_len != float('inf') else 0