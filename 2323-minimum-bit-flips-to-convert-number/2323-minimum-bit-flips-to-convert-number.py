class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans = start ^ goal
        count = 0
        for i in range(31):  # up to bit 30 is enough
            if ans & (1 << i):
                count += 1
        return count