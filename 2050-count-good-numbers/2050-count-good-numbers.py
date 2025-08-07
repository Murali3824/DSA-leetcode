class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9+7

        def pow(x,n):
            if n == 0:
                return 1
            res = 1
            while n > 1:
                if n % 2 != 0: # odd power
                    res = res * x % mod
                n = n // 2
                x = (x*x) % mod
            return res * x  #(5^1)
        
        even = ceil(n/2)
        odd = n // 2

        return (pow(5,even)*pow(4,odd)) % mod