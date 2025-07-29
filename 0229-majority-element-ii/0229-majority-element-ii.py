class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = {}
        res = []
        for num in nums:
            freq[num] = freq.get(num,0) + 1
            if freq[num] > n // 3:
                if num not in res:
                    res.append(num)
        return res