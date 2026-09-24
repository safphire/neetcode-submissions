class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixProd = [1] * n
        postfixProd = [1] * n
        pre, post = 1, 1
        for i in range(n):
            j = n - 1 - i
            prefixProd[i] = pre
            postfixProd[j] = post
            pre *= nums[i]
            post *= nums[j]

        res = [0] * n
        for i in range(n):
            res[i] = prefixProd[i] * postfixProd[i]
        return res
        