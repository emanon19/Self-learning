class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums or len(nums) < 4:
            return []
        s = set()
        length = len(nums)
        nums.sort()

        for i in range(length-3):
            for j in range(i+3,length):
                left, right = i+1, j-1
                while left < right:
                    if (nums[i]+nums[j]+nums[left]+nums[right]) == target:
                        s.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1
                    elif (nums[i]+nums[j]+nums[left]+nums[right]) < target:
                        left += 1
                    elif (nums[i]+nums[j]+nums[left]+nums[right]) > target:
                        right -= 1
        return list(s)
            
