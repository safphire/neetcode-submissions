class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProd = [1] * len(nums)
        postfixProd = [1] * len(nums)
        pre, post = 1, 1
        for i in range(len(nums)):
            pre *= nums[i]
            post *= nums[len(nums) - 1 - i]
            prefixProd[i] = pre
            postfixProd[len(nums) - 1 - i] = post

        res = [0] * len(nums)
        res[0] = postfixProd[1]
        res[len(nums) - 1] = prefixProd[len(nums)-2]
        for i in range(1, len(nums)-1):
            res[i] = prefixProd[i-1] * postfixProd[i+1]
        return res
        