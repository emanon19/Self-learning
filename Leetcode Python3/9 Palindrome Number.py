class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x % 10 == 0 and x != 0:
            return False
        elif 0<x<2:
            return True
        else:
            res = 0
            while x > res:
                res = res * 10 + x % 10
                x = x // 10
            return True if (x == res or x == res // 10) \
                        else False



nums = [121, -121, 10]

sol = Solution()
for i in range(3):
    print(sol.isPalindrome(nums[i]))
