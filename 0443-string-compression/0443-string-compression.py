class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        count = 1

        for j in range(1,len(chars)+1):
            if j == len(chars) or chars[j-1] != chars[j]:
                chars[i] = chars[j-1]
                i += 1
                if count >= 2:
                    for digit in str(count):
                        chars[i] = digit
                        i += 1
                count = 1
            else:
                count += 1
        return i