class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum, minSum = nums[0], nums[0]
        currMax, total, currMin = 0, 0, 0
        for n in nums:
             currMin = min(currMin + n, n)
             currMax = max(currMax + n, n)
             maxSum = max(currMax, maxSum)
             minSum = min(currMin, minSum)
             total += n

        return maxSum if maxSum < 0 else max(maxSum, (total - minSum))