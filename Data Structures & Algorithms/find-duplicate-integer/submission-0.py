class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        cache = set()
        for i in nums:
            if i in cache:
                return i
            cache.add(i)