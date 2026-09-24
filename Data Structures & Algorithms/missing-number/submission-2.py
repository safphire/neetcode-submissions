class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        actual_sum = 0
        final_sum = 0
        for n in nums:
            final_sum += n
        for i in range(0, len(nums) + 1):
            actual_sum += i
        return actual_sum - final_sum