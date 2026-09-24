class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        if nums[l] < nums[r]:
            return nums[l]
        while l <= r:
            if l == r:
                return nums[l]
            m = (r + l) // 2
            if nums[m] > nums[m + 1]:
                return nums[m + 1]
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m
        return nums[l]