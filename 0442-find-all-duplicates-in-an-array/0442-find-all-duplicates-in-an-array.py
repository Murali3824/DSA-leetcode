class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq = {}
        res = []
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                if num not in res:
                    res.append(num)
        return res if res else []