class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        options = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = []

        def backtrack(num_str, output):
            if not num_str:  # all digits processed
                res.append(output)
                return
            
            # process first digit
            n1 = int(num_str[0])
            for ch in options[n1]:
                backtrack(num_str[1:], output + ch)

        backtrack(digits, "")
        return res
