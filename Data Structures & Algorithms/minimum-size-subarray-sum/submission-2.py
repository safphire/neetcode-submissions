class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        r, l = 0, 0
        minlen = len(nums) + 1
        currSum = 0
        while r < len(nums):
            currSum += nums[r]
            while currSum >= target:
                print(minlen)
                minlen = min(minlen, r - l + 1)
                currSum -= nums[l]
                l += 1
            r += 1
        return 0 if minlen == len(nums) + 1 else minlen