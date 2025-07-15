class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        prefixMax = [0] * n
        suffixMax = [0] * n

        prefixMax[0] = height[0]
        for i in range(1, n):
            prefixMax[i] = max(prefixMax[i - 1], height[i])

        suffixMax[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            suffixMax[i] = max(suffixMax[i + 1], height[i])

        total = 0
        for i in range(n):
            leftmax, rightmax = prefixMax[i], suffixMax[i]
            if (height[i] < leftmax) and height[i] < rightmax:
                total += min(leftmax,rightmax) - height[i]
        return total