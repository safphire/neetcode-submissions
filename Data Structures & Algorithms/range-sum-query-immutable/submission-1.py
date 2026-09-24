class NumArray:
    presum = [0]
    def __init__(self, nums: List[int]):
        self.presum = [0] * len(nums)
        currSum = 0
        for i in range(0, len(nums)):
            currSum += nums[i]
            self.presum[i] = currSum
        

    def sumRange(self, left: int, right: int) -> int:
        return self.presum[right] - self.presum[left-1] if left > 0 else self.presum[right]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)