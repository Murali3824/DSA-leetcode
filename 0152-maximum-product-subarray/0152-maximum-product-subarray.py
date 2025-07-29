class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #product = 0
        #if len(nums) == 1:
        #    product = nums[0]
        #for i in range(len(nums)):
        #    arr = []
        #    for j in range(i,len(nums)):
        #        arr.append(nums[j])
        #        product = max(product,math.prod(arr))
        #return product

        max_product = float('-inf')
        left_prod = 1
        right_prod = 1
        n = len(nums)
        
        for i in range(n):
            left_prod *= nums[i]
            right_prod *= nums[n - 1 - i]
            
            max_product = max(max_product, left_prod, right_prod)
            
            if left_prod == 0:
                left_prod = 1
            if right_prod == 0:
                right_prod = 1
        
        return max_product

        