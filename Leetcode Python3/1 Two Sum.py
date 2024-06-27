class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hm = {}
        l = len(nums)
        for i in range(l):
            hm[nums[i]] = i
        for i in range(l):
            remain = target - nums[i]
            if remain in hm and hm[remain] != i:
                return [i, hm[remain]]

num1 = [2,7,11,15]
num2 = [3,2,4]
num3 = [3,3]

nums = [num1, num2, num3]
target = [9, 6, 6]


sol = Solution()
for i in range(3):
    print(sol.twoSum(nums[i], target[i]))
