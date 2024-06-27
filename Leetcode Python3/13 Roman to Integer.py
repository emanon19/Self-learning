Dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

class Solution:
    def romanToInt(self, s: str) -> int:
        Result = 0
        s = s.replace('IV', 'IIII') \
        .replace('IX', 'VIIII') \
        .replace('XL', 'XXXX')  \
        .replace('XC', 'LXXXX') \
        .replace('CD', 'CCCC')  \
        .replace('CM', 'DCCCC')

        for i in range(len(s)):
            Result += Dict[s[i]]
        return Result

sol = Solution()
print(sol.romanToInt('III'))
print(sol.romanToInt('IV'))
print(sol.romanToInt('VIII'))


class Solution:
    def romanToInt(self, s: str) -> int:
        Result = 0

        for i in range(len(s) - 1):
            if Dict[s[i]] < Dict[s[i+1]]:
                Result -= Dict[s[i]]
            else:
                Result += Dict[s[i]]
        Result += Dict[s[-1]]
        return Result

sol = Solution()
print(sol.romanToInt('III'))
print(sol.romanToInt('IV'))
print(sol.romanToInt('VIII'))
