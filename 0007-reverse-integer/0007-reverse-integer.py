class Solution:
    def reverse(self, n: int) -> int:
        negative = n < 0
        if negative:
            n = -n 
        else:
            n
        r = 0
        while n > 0:  
            l = n % 10  
            n //= 10 
            r = (r * 10) + l 

        if negative:
            r = -r
        if r < -2**31 or r > 2**31 - 1:
            return 0

        return r
