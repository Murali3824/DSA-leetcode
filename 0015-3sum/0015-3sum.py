class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()  
        arr = []

        if n < 3:
            arr = []

        for i in range(n): 
            if i > 0 and nums[i] == nums[i-1]:  
                continue
            j = i + 1
            k = n - 1  
            while j < k:
                sums = nums[i] + nums[j] + nums[k]
                if sums < 0:
                    j += 1
                elif sums > 0:
                    k -= 1
                else:
                    temp = [nums[i], nums[j], nums[k]]
                    arr.append(temp)
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return arr