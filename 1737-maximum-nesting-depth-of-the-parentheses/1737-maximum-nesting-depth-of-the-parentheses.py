class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        depth = 0
        for i in range(len(s)):
            if s[i] == '(':
                count += 1
                depth = max(depth,count)
            if s[i] == ')':
                count -= 1
        return depth    
