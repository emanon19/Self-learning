class Solution:
    def shortestPalindrome(self, s: str) -> str:
        reverse = s[::-1]
        for i in range(len(reverse)):
            pattern = reverse[i:]
            if pattern == s[:len(s)-i]:
                if pattern:
                    return reverse[:i] + s
        return ''
