class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)

        if target < nums[left]:
            return 0
        if target > nums[right - 1]:
            return len(nums)
        
        while left <= right:
            mid = (left + right) // 2
            if target < nums[mid]:
                right = mid - 1
            if target > nums[mid]:
                left = mid + 1
            if target == nums[mid]:
                return mid
        return left
        