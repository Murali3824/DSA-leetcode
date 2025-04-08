class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        temp = []
        for i in range(n-k,n):
            temp.append(nums[i])
        for i in range(n-k-1,-1,-1):
            nums[i+k] = nums[i]
        for i in range(k):
            nums[i] = temp[i]


        