class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        maxlen = len(res)

        i = 0
        while i < len(s):
            curchar = s[i]
            cur = i + 1
            while cur < len(s) and s[cur] == s[i]:
                cur += 1 
            tmp = curchar * (cur - i)
            left, right = i, cur-1
            i = cur
            if len(tmp) > len(res):
                res = tmp
            
            while left > 0 and right < len(s) - 1:
                left -= 1
                right += 1
                if s[left] == s[right]:
                    tmp = s[left] + tmp + s[right]
                    if len(tmp) > len(res):
                        res = tmp
                else:
                    break
        return res
