class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums)-1
        while i>0 and nums[i-1]>=nums[i]:
            i-=1
        if i<1:
            # nums[:] = nums[::-1]
            nums.reverse()
        else:
            j = len(nums)-1
            while nums[j]<=nums[i-1]:
                j-=1
            nums[j],nums[i-1] = nums[i-1],nums[j]
            # nums[i:] = nums[i:][::-1]
            nums[i:] = reversed(nums[i:])
        