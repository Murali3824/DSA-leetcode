class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        #def is_palindrome(sub):
        #    return sub == sub[::-1]

        def is_palindrome(start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
    
        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])
                return
            
            for end in range(start, len(s)):
                #if is_palindrome(s[start:end+1]):
                if is_palindrome(start, end):
                    path.append(s[start:end+1])
                    backtrack(end+1, path)
                    path.pop()
        
        backtrack(0, [])
        return result