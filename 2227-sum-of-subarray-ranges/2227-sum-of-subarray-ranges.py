class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)

        min_sum = 0
        stack1 = []

        for i in range(n + 1):
            cur = nums[i] if i < n else float('-inf')  # sentinel
            while stack1 and nums[stack1[-1]] > cur:
                mid = stack1.pop()
                left = stack1[-1] if stack1 else -1
                right = i
                count = (mid - left) * (right - mid)
                min_sum += nums[mid] * count
            stack1.append(i)

        max_sum = 0
        stack2 = []

        for i in range(n + 1):
            cur = nums[i] if i < n else float('inf')  # sentinel
            while stack2 and nums[stack2[-1]] <= cur:
                mid = stack2.pop()
                left = stack2[-1] if stack2 else -1
                right = i
                count = (mid - left) * (right - mid)
                max_sum += nums[mid] * count
            stack2.append(i)

        return max_sum - min_sum
