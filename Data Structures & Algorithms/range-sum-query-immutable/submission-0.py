class NumArray:
    presum = [0]
    def __init__(self, nums: List[int]):
        self.presum = [0] * len(nums)
        currSum = 0
        self.presum[0] = nums[0]
        for i in range(1, len(nums)):
            self.presum[i] = self.presum[i-1] + nums[i]
        

    def sumRange(self, left: int, right: int) -> int:
        return self.presum[right] - self.presum[left-1] if left > 0 else self.presum[right]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)