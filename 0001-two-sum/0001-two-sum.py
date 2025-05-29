class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        arr = []
        for i in range(n):
            for j in range(i,n):
                if nums[i] + nums[j] == target and i != j:
                    arr.append(i)
                    arr.append(j)
        return arr
        