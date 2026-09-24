class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        r, l = 0, 0
        while r < len(nums):
            count = 0
            nums[l] = nums[r]
            while r < len(nums) and nums[l] == nums[r]:
                    r += 1
                    count += 1
            if count >= 2:
                nums[l+1] = nums[l]
                l+=1
            l += 1
        return l